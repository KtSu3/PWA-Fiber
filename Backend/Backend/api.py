from ninja import NinjaAPI
from django.db import connections
from API.models import FirstQuery, SecondQuery, ClientQuery, PowerVerificationQuery
import uuid
from datetime import datetime, timedelta
from django.utils.timezone import now
import uuid
from decimal import Decimal
import time
from django.http import JsonResponse
from django.db import connections
from netmiko import ConnectHandler

api = NinjaAPI()
timesiries = time.time()
old = int(timesiries - timedelta(hours=1).total_seconds())


@api.get('/client')
def client(request, client: str, user: str):
    with connections['postgres'].cursor() as cursor:
        query = f"""
        WITH cte_status AS (
            SELECT
                split_part(items.key_, '[', 2) AS split_part,
                split_part(items.name, 'Model', 1) AS cliente,
                split_part(items.key_, '[', 2) AS slot,
                hosts.name AS host_name,
                interface.ip AS ip_host
            FROM history_uint
            JOIN items ON history_uint.itemid = items.itemid
            JOIN hosts ON items.hostid = hosts.hostid
            JOIN interface ON hosts.hostid = interface.hostid
            WHERE items.key_ LIKE 'onustatus%'
              AND split_part(items.name, 'Model', 1) LIKE '%{client}%'
        ),
        cte_final_status AS (
            SELECT
                DISTINCT ON (split_part)
                split_part,
                split_part(slot, '.', 1)::NUMERIC AS slot,
                cliente,
                replace(split_part(split_part, '.', 2), ']', '') AS clienteid,
                host_name,
                ip_host
            FROM cte_status
        ),
        cte_joined AS (
            SELECT 
                s.split_part,
                split_part(z.pon, '/', 2)::TEXT AS slot,
                split_part(z.pon, '/', 3)::TEXT AS pon,
                s.cliente,
                s.clienteid,
                s.host_name,
                s.ip_host
            FROM cte_final_status s
            JOIN zte_slot_pon z ON s.slot = z.oid::NUMERIC
        )
        SELECT 
            slot,
            pon, 
            clienteid, 
            cliente, 
            ip_host
        FROM cte_joined
        ORDER BY slot ASC, pon ASC;
        """
        cursor.execute(query)
        results = cursor.fetchall()
    
    if not results:
        return {"error": "Nenhum cliente encontrado."}
    
    data = []
    data_to_save = []
    query_id = uuid.uuid4()
    
    for result in results:
        slot, pon, clienteid, cliente, device = result
        
        

        device_info = {
            "device_type": "zte_zxros",
            "host": device,
            "username": "kaua.mendes",
            "password": "adM!*#18",
            "port": 22,
        }
        connection = ConnectHandler(**device_info)
        onu_info = {
            'name': cliente,
            'slot': slot,
            'pon': pon,
            'onu': clienteid,
            'onu_distance': '',
            'status': '',
            'signal': '',
            'authpass_history': []
        }
        
        detail_command = f'show gpon onu detail-info gpon_onu-1/{slot}/{pon}:{clienteid}'
        detail_output = connection.send_command(detail_command)
        
        power_command = f'show pon power attenuation gpon_onu-1/{slot}/{pon}:{clienteid}'
        power_output = connection.send_command(power_command)
        
        parsing_table = False
        for line in detail_output.splitlines():
            if "Name:" in line:
                onu_info['name'] = line.split(":", 1)[1].strip()
            elif "Phase state:" in line:
                onu_info['status'] = line.split(":", 1)[1].strip()
            elif "ONU Distance:" in line:
                onu_info['onu_distance'] = line.split(":", 1)[1].strip()
            elif "Authpass Time" in line and "OfflineTime" in line:
                parsing_table = True  # Inicia a extração da tabela
            elif parsing_table:
                parts = line.split()
                if len(parts) >= 3:
                    authpass_time = f"{parts[1]} {parts[2]}"
                    offline_time = f"{parts[3]} {parts[4]}" if len(parts) >= 5 else ""
                    cause = parts[5] if len(parts) >= 6 else "Unknown"
                    onu_info['authpass_history'].append({
                        "authpass_time": authpass_time,
                        "offline_time": offline_time,
                        "cause": cause
                    })
        
        for line in power_output.splitlines():
            if "Rx:" in line:
                onu_info['signal'] = line.split("Rx:")[1].split()[0].strip()

        connection.disconnect()

        data_to_save.append(ClientQuery(
            query_id=query_id,
            name=onu_info['name'],
            slot=onu_info['slot'],
            pon=onu_info['pon'],
            onu=onu_info['onu'],
            onu_distance=onu_info['onu_distance'],
            status=onu_info['status'],
            signal=onu_info['signal'],
            user=user
        ))

    ClientQuery.objects.bulk_create(data_to_save)
    data.append(onu_info)

    return {"data": data, "user": user}
