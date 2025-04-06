from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from account.models import User
from article.models import Article, Category
from article.views import ArticleDetailView, ArticleListView, ArticleAddView


class ArticleUrlsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.phone = '1234'
        cls.password = '1234'
        cls.author = User.objects.create(phone=cls.phone, password=cls.password)
        cls.category = Category.objects.create(title='life')
        cls.article = Article.objects.create(author=cls.author, category=cls.category, title='life', text='is good')

    def test_article_detail(self):
        url = reverse('article:detail', args=[self.article.pk])
        self.assertEqual(resolve(url).func.view_class, ArticleDetailView)

    def test_article_list_url(self):
        url = reverse('article:list')
        self.assertEqual(resolve(url).func.view_class, ArticleListView)

    def test_add_article_url(self):
        url = reverse('article:add')
        self.assertEqual(resolve(url).func.view_class, ArticleAddView)


