from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'apps.blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<slug:slug>-<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]
