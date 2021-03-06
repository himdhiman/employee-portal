from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_Name, last_Name, gender, salary, password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_Name = first_Name,
            last_Name = last_Name,
            gender = gender,
            salary = salary
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, first_Name, last_Name, gender, salary, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_Name = first_Name,
            last_Name = last_Name,
            gender = gender,
            salary = salary,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self._db)
        return user



class CustomUser(AbstractBaseUser):

    gender_choices = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others")
    )

    email = models.EmailField(verbose_name = "email", unique = True, max_length = 60)
    first_Name = models.CharField(max_length = 20)
    last_Name = models.CharField(max_length = 20)
    joining_Date = models.DateField(auto_now = True, verbose_name = "date joined")
    gender = models.CharField(max_length = 1, choices = gender_choices)
    salary = models.IntegerField()
    last_login = models.DateField(auto_now = True, verbose_name = "last login")
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_Name', 'last_Name', 'gender', 'salary']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True





