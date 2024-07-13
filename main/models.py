from django.db import models


class Dolzn(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class AdvUser(models.Model):
    name = models.CharField('Имя пользователя', max_length=255)
    dolzn = models.ForeignKey(
        Dolzn,
        on_delete=models.CASCADE,
        verbose_name='Должность',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class WebSystem(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Вэб-система'
        verbose_name_plural = 'Вэб-системы'

    def __str__(self):
        return self.name


class Protocol(models.Model):
    date = models.DateTimeField("Дата")
    time = models.IntegerField("Время в минутах")
    traffic = models.IntegerField("Трафик")
    user = models.ForeignKey(AdvUser,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    websystem = models.ForeignKey(WebSystem,
                                  on_delete=models.CASCADE,
                                  verbose_name="Система")

