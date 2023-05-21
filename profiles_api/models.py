from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create Model Manager
class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have a email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name= name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create a new super user with given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Database Model for Users in System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    #active profiles vs deactive
    is_active = models.BooleanField(default=True)
    #staff users for django admin
    is_staff = models.BooleanField(default=False)
    
    #Model manager to manage users
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self) -> str:
        """Return string representation of our user"""
        return self.email + ' :' + self.name

    