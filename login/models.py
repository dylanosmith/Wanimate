from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.

class UserManager (models.Manager):
    def basic_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(postData["email"]):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"

        #add keys and values to errors dictionary for each invalid field

        if len(postData["fname"]) < 2 or postData["fname"].isalpha() == False:
            errors["fname"] = "first name needs to be atleast 2 characters, letters only"

        if len(postData["lname"]) < 2 or postData["lname"].isalpha() == False:
            errors["lname"] = "last name needs to be atleast 2 characters, letters only"
        
        if len(postData["password"]) < 8:
            errors["password_length"] = "password must be longer than 8 characters"
        
        if postData["password"] != postData["password_conf"]:
            errors["password_match"] = "both password fields must match"

        # if received_date > today:
        #     errors["release_date"] = "Show's release date must occur in the past"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()