from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


__all__ = (
    'facebook_login_backup',
)

def facebook_login_backup(request):
    code = request.GET.get('code')
    user = authenticate(request, code=code)
    login(request, user)
    return redirect('crawler')
