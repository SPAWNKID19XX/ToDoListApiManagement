from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
  def create(self, email = None, password = None, **extra_fields):
    if (not email) or (email == None):
      raise ValueError("Email is required and can not be None")
    
    if (not password) or (password==None):
      raise ValueError("Password is required and can not be None")

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def createsuperser(self, email = None, password = None, **extra_fields):
    if (not email) or (email == None):
      raise ValueError("Email is required and can not be None")
        
    if (not password) or (password==None):
      raise ValueError("Password is required and can not be None")
  
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    extra_fields.setdefault('is_admin', True)
    extra_fields.setdefault('is_superuser', True)
    user.save(using=self._db)
    return user
    

class CustomUser(AbstractUser): 
  username = None
  email = models.EmailField(unique=True)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = UserManager()
  
