from ninja import NinjaAPI
from pydantic import BaseModel
from django.db import IntegrityError
from django.http import JsonResponse
from API.models import User
import requests
import hashlib

api_login = NinjaAPI(urls_namespace='api_login')

class ExternalLoginSchema(BaseModel):
    email: str
    password: str

class UserSchema(BaseModel):
    username: str
    email: str
    grup: int
    password: str


@api_login.post("/login/")
def login_external(request, data: ExternalLoginSchema):
    sha256_hash = hashlib.sha256(data.password.encode('utf-8')).hexdigest()

    external_url = f"urlAtenticationExternal"

    try:
        external_response = requests.get(external_url)
        external_response.raise_for_status()
        external_data = external_response.json()
    except requests.RequestException as e:
        return JsonResponse({"error": f"Erro ao conectar à API externa: {str(e)}"}, status=400)

    try:
        user, created = User.objects.update_or_create(
            email=external_data["email"],
            defaults={
                "username": external_data["nome"],
                "grup": external_data["grupo"],
                "password": sha256_hash,
            },
        )
        response_data = {
            "message": "Usuário autenticado com sucesso.",
            "user": {
                "username": user.username,
                "email": user.email,
                "grup": user.grup,
            },
            "created": created,
        }
        return JsonResponse(response_data, status=200)
    except IntegrityError:
        return JsonResponse({"error": "Erro ao criar/atualizar usuário."}, status=500)

