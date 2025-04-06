from rest_framework.test import APITestCase
from account.models import User
from article.models import Article, Category
from django.utils.translation import gettext_lazy as _


class CategoryModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(title='life category')

    def test_title_label(self):
        field_label = self.category._meta.get_field('title').verbose_name
        self.assertEqual(field_label, _('title'))


class ArticleModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(phone='1234', password='1234')
        cls.category = Category.objects.create(title='category')
        cls.article = Article.objects.create(author=cls.author, title='life', category=cls.category, text='is good')

    def test_author_label(self):
        field_label = self.article._meta.get_field('author').verbose_name
        self.assertEqual(field_label, _('نویسنده'))

    def test_title_label(self):
        field_label = self.article._meta.get_field('title').verbose_name
        self.assertEqual(field_label,_('عنوان مقاله'))

    def test_text_label(self):
        field_label = self.article._meta.get_field('text').verbose_name
        self.assertEqual(field_label,_('متن'))

    def test_image_label(self):
        field_label = self.article._meta.get_field('image').verbose_name
        self.assertEqual(field_label,_('عکس'))
