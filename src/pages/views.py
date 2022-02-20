from django.shortcuts import render
from . import models as pagemodel
from config import models as configmodel
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    context = {
        'header': configmodel.Header.objects.filter(HeaderStatus='Publish'),
        'articles': pagemodel.Article.objects.filter(ArticleStatus='Publish').order_by('-ArticleDate'),
        'sub': configmodel.Sub.objects.filter(SubStatus='Publish'),
        'media': configmodel.Media.objects.filter(MediaStatus='Publish'),
    }
    return render(request, 'pages/index.html', context)

def Post(request, slug):
    context = {
    'article': pagemodel.Article.objects.get(ArticleSlug=slug),
    }
    return render(request, 'pages/post.html', context)

def AboutMe(request):
    context = {
        'aboutme': pagemodel.Aboutme.objects.all(),
    }
    return render(request, 'pages/aboutme.html', context)

def Projects(request):
    context = {
        'projects': pagemodel.Projects.objects.filter(ProjectStatus='Publish').order_by('-ProjectDate'),
    }
    return render(request, 'pages/projects.html', context)

def Contact(request):
    context = {
        'contact': pagemodel.Contact.objects.all(),
    }
    return render(request, 'pages/contact.html', context)

def Support(request):
    context = {
        'supports':
            #pagemodel.Support.objects.all(),
            pagemodel.Support.objects.filter(SupportStatus='Publish').order_by('SupportDate'),
    }
    return render(request, 'pages/support.html', context)

def Blogs(request):
    articles_list = pagemodel.Article.objects.filter(ArticleStatus='Publish').order_by('-ArticleDate')
    paginator = Paginator(articles_list, 6)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    context = {
        'articles': articles,
    }
    return render(request, 'pages/blogs.html', context)

def Base(request):
    context = {
        'category': pagemodel.Category.objects.all(),
    }
    return render(request, 'pages/base.html', context)

def Category(request, slug):
    context = {
        'category': pagemodel.Category.objects.get(CategorySlug=slug) ,
    }
    return render(request, 'pages/categorypage.html', context)