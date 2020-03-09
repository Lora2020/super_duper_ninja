from django.db import models



# Create your models here.
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(postData['email']) < 3:
            errors['email'] = "Network name should be at least 3 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['password']!= postData ['confirm_PW']:
            errors ['password'] = "password should be the same"
        return errors

        

class Users(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()
    

class Message(models.Model):
    user = models.ForeignKey(Users, related_name='Messages', on_delete=models.CASCADE)
    message_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message_id = models.ForeignKey(Message, related_name='message_comments', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, related_name='user_comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)