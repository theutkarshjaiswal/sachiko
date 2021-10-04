from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    first_name = models.CharField(max_length = 120, blank = True, null = True)
    last_name = models.CharField(max_length = 120, blank = True, null = True)
    username = models.CharField(max_length = 120, blank = True, null = True)
    email = models.EmailField(_('email address'), unique = True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    date_joined = models.DateTimeField(default = timezone.now)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email 


class Category(models.Model):
    category = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.category


class Game(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    category = models.ManyToManyField(Category)
    image =  models.URLField(max_length=200, blank = True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    start_date = models.DateTimeField()

    def __str__(self):
        return self.user.username