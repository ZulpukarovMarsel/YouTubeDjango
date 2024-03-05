from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.user.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=45, verbose_name="Имя")
    lastname = models.CharField(max_length=45, verbose_name="Фамилия")
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')
    image = models.ImageField(blank=True, verbose_name="Аватар", upload_to="user_photo/", default="/user_photo"
                                                                                                  "/default_photo"
                                                                                                  "/default_user.jpg")
    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)
    data_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'

class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='channel')
    subscribers = models.ManyToManyField(User, related_name='subscribed_channels', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name