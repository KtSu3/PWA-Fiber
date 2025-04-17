from django.db import models
from django.contrib.auth.hashers import make_password
import uuid
from django.contrib.auth.models import AbstractBaseUser
from dirtyfields import DirtyFieldsMixin 
class DatabaseRouter:

    def db_for_read(self, model, **hints):
        #direcionamento de leitura
        if model.__name__ in ['FirstQuery', 'SecondQuery', 'User' ]:
            return 'default'
        return 'postgres'

    def db_for_write(self, model, **hints):
        #escritas para default
        if model.__name__ in ['FirstQuery', 'SecondQuery', 'User']:
            return 'default'
        return 'postgres'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite relacionamentos apenas no banco 'default'.
        """
        db_list = ('default',)
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
       #Migrações de Tabela
        if model_name in ['firstquery', 'secondquery', 'user']:
            return db == 'default'
        return db == 'postgres'

class User(AbstractBaseUser, DirtyFieldsMixin):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    grup = models.IntegerField(null=True, blank=True)
    login = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.pk or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    class Meta:
        db_table = 'API_user'

class FirstQuery(models.Model):
    name = models.CharField(max_length=255)
    slot = models.IntegerField()
    pon = models.IntegerField()
    onu = models.IntegerField()
    onu_distance = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    signal = models.CharField(max_length=50)
    query_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.CharField(User,max_length=150)
    data = models.DateTimeField(auto_now=True)
    
class SecondQuery(models.Model):
    name = models.CharField(max_length=255)
    slot = models.IntegerField()
    pon = models.IntegerField()
    onu = models.IntegerField()
    onu_distance = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    signal = models.CharField(max_length=50)
    query_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now=True)

class PowerVerificationQuery(models.Model):
    name = models.CharField(max_length=255)
    slot = models.IntegerField()
    pon = models.IntegerField()
    onu = models.IntegerField()
    onu_distance = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    signal = models.CharField(max_length=50)
    query_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now=True)

class ClientQuery(models.Model):
    name = models.CharField(max_length=255)
    slot = models.IntegerField()
    pon = models.IntegerField()
    onu = models.IntegerField()
    onu_distance = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    signal = models.CharField(max_length=50)
    query_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now=True)

class FiberQuery(models.Model):
    fibra = models.CharField(max_length=255)
    olt = models.CharField(max_length=255)
    user = models.CharField(max_length=150)
    query_id = models.UUIDField(default=uuid.uuid4, editable=False)
    data = models.DateTimeField(auto_now=True)

class LogSearch(models.Model):
    search = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now=True)

