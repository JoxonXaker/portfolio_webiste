from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class HistoryPageView(TemplateView):
    template_name = 'history.html'


class ArticlesPageView(TemplateView):
    template_name = 'articles.html'


class ArticleDetailPageView(TemplateView):
    template_name = 'article_detail.html'


class ProjectsPageView(TemplateView):
    template_name = 'projects.html'


class ProjectDetailPageView(TemplateView):
    template_name = 'project_detail.html'

