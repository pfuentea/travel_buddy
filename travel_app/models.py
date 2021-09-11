from django.db import models
import re
from datetime import date

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 3:
            errors['name_len'] = "Nombre debe tener al menos 3 caracteres de largo"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "correo invalido"
            
        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "solo letras en nombre por favor"

        if len(postData['password']) < 8:
            errors['password'] = "contraseña debe tener al menos 8 caracteres"

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        return errors

class TravelManager(models.Manager):
    def validador_basico(self, postData):
        errors = {}
        today= date.today().strftime('%Y-%m-%d')
        if len(postData['destination']) < 1:
            errors['destionation_len'] = "Debes agregar un Destination"
        if len(postData['description']) < 1:
            errors['description_len'] = "Debes agregar una Description"
        if postData['date_init'] < today:    
            errors["date_init"] ="La fecha inicial debe ser superior a hoy"
        if postData['date_init'] > postData['date_end']:    
            errors["date_init"] ="La fecha final no puede ser inferior a la inicial"
        
        return errors

class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=255, choices=CHOICES)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Travel(models.Model):
    destination = models.CharField(max_length=100)
    plan = models.CharField(max_length=500)
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    creator = models.ForeignKey(User, related_name="creados", on_delete = models.CASCADE)
    fellows = models.ManyToManyField(User, related_name="planificados")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = TravelManager()