from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length="150", verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    creations_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания', editable=False)
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name="Категории", on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-creations_date']

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"