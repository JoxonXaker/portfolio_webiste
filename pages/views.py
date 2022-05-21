from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from account.models import User, UserSpecialization, Specialization


# class HomePageView(ListView):
#     template_name = 'home.html'
#     model = User


def HomePageView(request):
    return render(
        request=request,
        template_name='home.html',
        context={
            'menu': 'Home',

        },
    )

def AuthUserPageView(request, username):
    user = User.objects.get(username=username)
    jobs = user.professions.all()
    langs = user.languages.all()
    specs = user.specials.all()
    addits = user.additionals.all()
    return render(
        request=request,
        template_name='home.html',
        context={
            'user': user,
            'job': [job for job in jobs],
            'langs': [langs for langs in langs],
            'specs': [specs for specs in specs],
            'addits': addits,
        }
    )


def ContactPageView(request, username):
    print('hello:***', request)
    return render(
        request=request,
        template_name='contact.html',
        context={
            'menu': 'Contact'
        },
    )


def ArticlesPageView(request, username):
    return render(
        request=request,
        template_name='articles.html',
        context={
            'menu': 'Blogs'
        },
    )


def HistoryPageView(request, username):
    print('hello:***', request)
    return render(
        request=request,
        template_name='history.html',
        context={
            'menu': 'History'
        },
    )


def ProjectsPageView(request, username):
    return render(
        request=request,
        template_name='projects.html',
        context={
            'menu': 'Projects'
        },
    )


def ProjectDetailPageView(request, username):
    print('hello:***', request)
    return render(
        request=request,
        template_name='project_detail.html',
        context={
            'menu': 'ProjectDetail'
        },
    )


def ArticleDetailPageView(request, username):
    return render(
        request=request,
        template_name='article_detail.html',
        context={
            'menu': 'BlogsDetail'
        },
    )

# class ContactPageView(TemplateView):
#     template_name = ''


# class HistoryPageView(TemplateView):
#     template_name = ''
#
#
# class ArticlesPageView(TemplateView):
#     template_name = ''
#
#
# class ArticleDetailPageView(TemplateView):
#     template_name = ''
#
#
# class ProjectsPageView(TemplateView):
#     template_name = ''
#
#
# class ProjectDetailPageView(TemplateView):
#     template_name = ''
