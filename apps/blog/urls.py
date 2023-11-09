from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'apps.blog'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('articles/<slug:slug>-<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]
