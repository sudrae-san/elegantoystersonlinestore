from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_admin=False, is_staff=False, is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a user name")

        user = self.model(
            email=self.normalize_email(email)
        )
        username = username
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email=self.normalize_email(email)
        )
        username = username
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username            = models.CharField(max_length=255)
    username            = models.CharField(max_length=255)
    email               = models.EmailField(max_length=255, unique=True,)
    gender              = models.CharField(max_length=255, blank=True, default='rather_not_say')
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login',auto_now=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'gender']  # Email & Password are required by default.

    objects = UserManager()

    def get_username(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
         # The user is identified by their email address
         return self.email

    def __str__(self):              # __unicode__ on Python 2
         return self.email

    @staticmethod
    def has_perm(perm, obj=None):
         # "Does the user have a specific permission?"
         # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
         # "Does the user have permissions to view the app `app_label`?"
         # Simplest possible answer: Yes, always
         return True

    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.staff

    @property
    def is_admin(self):
         # "Is the user a admin member?"
         return self.admin

    @property
    def is_active(self):
         # "Is the user active?"
         return self.active
