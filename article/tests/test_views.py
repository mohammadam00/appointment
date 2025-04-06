from rest_framework.test import APITestCase
from account.models import User
from article.models import Article, Category
from django.urls import reverse
from rest_framework import status
class ArticleDetailTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(phone='1234', password='1234')
        cls.category = Category.objects.create(title='life')
        cls.article = Article.objects.create(author=cls.author, category=cls.category, title='life', text='is goood')

    def test_article_detail_view(self):
        url = reverse('article:detail',args=[self.article.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_article_list_view(self):
        url = reverse('article:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_add_article_view(self):
        url = reverse('article:add')
        response = self.client.post(url)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
