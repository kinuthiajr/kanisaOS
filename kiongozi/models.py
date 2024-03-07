from django.db import models

# extend django user
# import 
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username required')
        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(
           email = self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name ='email',unique=True,max_length=90)
    username = models.CharField(max_length=50,unique=True)
    date_joined = models.DateField(auto_now_add=True,verbose_name='date joined')
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # tie the manager to the user
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    #overiding defaults in AbstractBaseUser

    def has_perm(self,perm,odj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True
    def soft_delete(self):
        self.is_active = False
        self.save()