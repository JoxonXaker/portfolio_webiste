from django.urls import path
from .views import (
    HomePageView,
    ContactPageView,
    HistoryPageView,
    ArticlesPageView,
    ArticleDetailPageView,
    ProjectsPageView,
    ProjectDetailPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('contact/', ContactPageView.as_view(), name='contactpage'),
    path('history/', HistoryPageView.as_view(), name='historypage'),
    path('articles/', ArticlesPageView.as_view(), name='articlespage'),
    path('article_detail/', ArticleDetailPageView.as_view(), name='article_detail'),
    path('projects/', ProjectsPageView.as_view(), name='projectspage'),
    path('project_detail/', ProjectDetailPageView.as_view(), name='project_detail'),

]
