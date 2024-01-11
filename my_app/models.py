from django.db import models

class MyUsers(models.Model):
    nickname = models.CharField('Нікнейм', max_length=60)
    password = models.TextField('Пароль')
    email = models.EmailField('Пошта')
    blog_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nickname}'
    
    class Meta():
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

class Blogs(models.Model):
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
    blog = models.TextField('Блог')

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.user.blog_count += 1
            self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.nickname} блог № {self.user.blog_count}'
    
    class Meta():
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'