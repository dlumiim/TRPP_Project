from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=1000)
    author = models.CharField('Авторы', max_length=25000)
    full_text = models.TextField('Статья')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
