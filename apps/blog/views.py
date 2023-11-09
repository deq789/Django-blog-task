from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    paginate_by = 5
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
