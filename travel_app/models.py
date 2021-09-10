from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validador_basico(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        SOLO_LETRAS = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 3:
            errors['name_len'] = "Nombre debe tener al menos 3 caracteres de largo";

        if len(postData['username']) < 3:
            errors['username_len'] = "Username debe tener al menos 3 caracteres de largo";

        if not SOLO_LETRAS.match(postData['name']):
            errors['solo_letras'] = "solo letras en nombre por favor"

        if len(postData['password']) < 4:
            errors['password'] = "contraseña debe tener al menos 8 caracteres";

        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "contraseña y confirmar contraseña no son iguales. "

        
        return errors


class User(models.Model):
    CHOICES = (
        ("user", 'User'),
        ("admin", 'Admin')
    )
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
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
    init_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, related_name="creados", on_delete = models.CASCADE)
    fellows = models.ManyToManyField(User, related_name="planificados")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    