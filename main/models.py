from django.db import models
from login.models import User

# Create your models here.

class Match(models.Model):
    cloud_only = models.BooleanField(default=False)
    prem_only = models.BooleanField(default=False)
    hybrid = models.BooleanField(default=False)
    international = models.BooleanField(default=False)
    low_latency = models.BooleanField(default=False)
    sla = models.BooleanField(default=False)
    firewall = models.BooleanField(default=False)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Vendor(models.Model):
    fk_match = models.ForeignKey(Match, related_name="vendors", on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    logo = models.CharField(max_length = 200)
    domain= models.CharField(max_length = 100)
    description = models.TextField()
    avg_rating = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    install_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Quote:
    fk_user = models.ForeignKey(User, related_name="quotes", on_delete = models.CASCADE)
    fk_vendor = models.ForeignKey(Vendor, related_name="quotes", on_delete = models.CASCADE)
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Review(models.Model):
    fk_user = models.ForeignKey(User, related_name="reviews", on_delete = models.CASCADE)
    fk_vendor = models.ForeignKey(Vendor, related_name="reviews", on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    star_rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

