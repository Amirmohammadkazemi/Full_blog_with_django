from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Account(request):
    return render(request, 'registration/account.html')