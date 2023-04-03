from django.shortcuts import render
from webapp.models import User

def account(request):
    profile = User.objects.get(user=request.user)
    return render(request, {'profile': profile})
