from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as _UserManager
from django.db import models

from app.files import RandomFileName


class User(AbstractUser):
    objects = _UserManager()  # type: _UserManager

    surname = models.CharField('Отчество', max_length=150, blank=True)
    avatar = models.ImageField('Аватар', upload_to=RandomFileName('avatars'), blank=True)
    position = models.CharField('Должность', max_length=255, blank=True)
    rank = models.CharField('Ранг', max_length=255, blank=True)
    phone = models.CharField('Телефонный номер', max_length=20, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    @property
    def full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.surname}'.strip()
