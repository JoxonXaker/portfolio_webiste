from django.urls import path
from .views import (
    HomePageView,
    ContactPageView,
    HistoryPageView,
    ArticlesPageView,
    ArticleDetailPageView,
    ProjectsPageView,
    ProjectDetailPageView,
    AuthUserPageView
)

urlpatterns = [
    path('', AuthUserPageView, name='auth_user_page'),
    path('', HomePageView, name='homepage'),
    path('contact/', ContactPageView, name='contactpage'),
    path('history/', HistoryPageView, name='historypage'),
    path('articles/', ArticlesPageView, name='articlespage'),
    path('article_detail/', ArticleDetailPageView, name='article_detail'),
    path('projects/', ProjectsPageView, name='projectspage'),
    path('project_detail/', ProjectDetailPageView, name='project_detail'),

]


