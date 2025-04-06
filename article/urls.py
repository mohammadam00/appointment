from django.urls import path
from .views import ArticleDetailView, ArticleListView, ArticleAddView

app_name = 'article'
urlpatterns = [
    path('<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('list', ArticleListView.as_view(), name='list'),
    path('add', ArticleAddView.as_view(), name='add'),
]
