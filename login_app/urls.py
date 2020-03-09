from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.add),
    path('add', views.add),
    path('done', views.done),
    path('login', views.login),
    path('index', views.logout),

    path('post_msg', views.the_wall),
    path('add_messages', views.add_messages),
    path('add_comments', views.add_comments),
    path('delete_msg/<int:msg_id>', views.delete_msg),
    path('delete_comment/<int:comment_id>', views.delete_comment),
]