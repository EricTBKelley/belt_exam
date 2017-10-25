# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..registration_app.models import User
from django.shortcuts import render,redirect
import ast

def friends(request):
    if 'email' not in request.session:
        return redirect('/')
    context = {
    "buddies": User.objects.get(id = request.session['id']).friends.all(),
    # "users": User.objects.exclude(User.objects.get(id = request.session['id']).friends.all()),
    "users": User.objects.exclude(id = (User.objects.get(id = request.session['id'])).friends.id),
    # .exclude(id = User.objects.get(id = request.session['id']).friends.all()),
    # "users": User.objects.exclude(User.objects.get(id = request.session['id']).friends.all())
    }
    return render(request, 'friends_app/friends.html', context)

def show(request, id):
    context = {
        "user": User.objects.get(id = id),
    }
    return render(request, 'friends_app/show.html',context)

def add(request, id):
    print User.objects.get(id = request.session['id']).f_name
    print User.objects.get(id = id).f_name
    you =  User.objects.get(id = request.session['id'])
    you.friends.add(User.objects.get(id = id))
    you.save()
    print you.friends.first().f_name
    return redirect('/friends')

def remove(request, id):
    you = User.objects.get(id = request.session['id'])
    your_friend = User.objects.get(id = id)
    you.friends.remove(your_friend)
    return redirect('/friends')
###change this next####
