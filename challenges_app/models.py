from django.db import models
import re


class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors={}
        if len(reqPOST['first_name'])< 2:
            errors['first_name'] = "Name must be at least 2 characters."
        if len(reqPOST['last_name'])< 2:
            errors['last_name'] = "Name must be at least 2 characters."
        if len(reqPOST['email'])< 6:
            errors['email'] = "Name must be at least 6 characters."
        if len(reqPOST['password'])< 8:
            errors['password'] = "Name must be at least 8 characters."
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['password_conf'] = "Password and password confirmation must match."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex'] = "Email in wrong format."
        user_with_email = User.objects.filter(email = reqPOST['email'])
        if len(user_with_email) >= 1:
            errors['duplicate']="Email taken, please use another."
        return errors

    def edit_validator(self, reqPOST, user_id):
        errors={}
        users_with_email = User.objects.filter(email=reqPOST['email']) #this will return a list, hence the next line using length
        if len(users_with_email)>=1:
            if user_id != users_with_email[0].id:
                errors['unique'] = "Email already taken."
        if len(reqPOST['first_name']) < 2:
            errors['name'] = "First name is too short, please use at least two characters."
        if len(reqPOST['last_name']) < 2:
            errors['last_name'] = "Last name is too short, please use at least two characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex'] = "Email in wrong format."
        return errors   

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    age = models.IntegerField(null = True)
    location = models.TextField(null = True)
    quote = models.TextField (null = True)
    goals = models.TextField(null = True)
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Challenge(models.Model):
    name = models.CharField(max_length = 45)
    description = models.TextField()
    target_area = models.CharField(max_length = 45)
    starting_at = models.TextField()
    daily_increase = models.TextField()
    max_reps = models.TextField()
    users_accepted = models.ManyToManyField(User, related_name="challenges_accepted")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = ChallengeManager()