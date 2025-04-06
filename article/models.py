from django.db import models

from account.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی ها')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='عنوان مقاله')
    text = models.TextField(verbose_name='متن')
    image = models.ImageField(verbose_name='عکس')
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title



