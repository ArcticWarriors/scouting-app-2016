'''
Created on Mar 28, 2016

@author: PJ
'''
from django.core.urlresolvers import reverse, reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def showLogin(request):

    return render(request, 'Scouting2016/login.html')


def log_user_out(request):
    logout(request)

    return HttpResponseRedirect(reverse('Scouting2016:showLogin'))


def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    good_redirect = request.POST.get('next', '/2016')
    bad_redirect = 'Scouting2016:showLogin'
    print good_redirect

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(good_redirect)
        else:
            return HttpResponseRedirect(reverse(bad_redirect))
    else:
        return HttpResponseRedirect(reverse(bad_redirect))
