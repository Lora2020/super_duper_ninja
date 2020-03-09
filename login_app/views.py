from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from .models import Users
from time import strftime, localtime
import datetime 

def index(request):
    return render(request, "index.html")

def add(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        NewUser = Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode())
        if 'userid' not in request.session:
            request.session['userid'] = NewUser.id
        request.session['userid'] = NewUser.id
        return redirect('/done')


def login(request):
    user = Users.objects.filter(email=request.POST['email'])
    if len(user) > 0: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/done')
    messages.error(request, "Invalid email/password", extra_tags="log")
    return redirect("/")


def done(request):
    if 'userid' not in request.session:
        return redirect('/')
    user = Users.objects.get(id=request.session['userid'])
    context = {
        'Users': user.first_name
    }
    return render(request,'done.html', context)
   

def logout(request):
    request.session.clear()
    return redirect('/')

def the_wall(request): 
    if 'userid' not in request.session:
        return redirect('/')
    user = Users.objects.get(id=request.session['userid'])
    message = Message.objects.all()
    comment = Comment.objects.all()
    context ={
        'first_name': user.first_name,
        'all_messages': message,
        'all_comments' : comment
    }
    return render(request, 'the_wall.html', context)


def add_messages(request):
    Message.objects.create(message_id=request.POST['message_id'], user = Users.objects.get(id=request.session['userid']))
    return redirect('/post_msg')


def add_comments(request):
    Comment.objects.create(comment= request.POST['comment'],user_id = Users.objects.get(id=request.session['userid']),message_id=Message.objects.get(id=request.POST['message_id']))
    return redirect('/post_msg')

def delete_msg (request, msg_id):
    delete_msg = Message.objects.get(id=msg_id)
    delete_msg.delete()
    return redirect('/post_msg')

def delete_comment (request, comment_id):
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('/post_msg')

