from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as _UserManager
from django.db import models


class User(AbstractUser):
    objects = _UserManager()  # type: _UserManager

    surname = models.CharField('Отчество', max_length=150, blank=True)
    position = models.CharField('Должность', max_length=255, blank=True)
    phone = models.CharField('Телефонный номер', max_length=20, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self) -> str:
        if not self.last_name and not self.first_name and not self.surname:
            return self.username
        return f'{self.last_name} {self.first_name} {self.surname}'.strip()
