from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'pages/index.html')

def AboutMe(request):
    return render(request, 'pages/aboutme.html')

def Projects(request):
    return render(request, 'pages/projects.html')

def Contact(request):
    return render(request, 'pages/contact.html')

def Support(request):
    return render(request, 'pages/support.html')

def Blogs(request):
    return render(request, 'pages/blogs.html')