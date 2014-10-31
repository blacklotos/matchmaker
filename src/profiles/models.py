from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField(max_length=5)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.city

class Job (models.Model):
    user = models.ForeignKey(User)
    position = models.CharField(max_length=200)
    employer = models.CharField(max_length=200)
    employer_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField(max_length=5)
    phone = models.CharField(max_length=20, null=True, blank=True)
    active =models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.position

class UserPicture (models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='profiles/')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.image)

CHOICES = (
    ('Regular', 'Regular'),
    ('Staff', 'Staff'),
    ('Premium','Premium'),
)

class UserRole (models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=120, default='Regular', choices=CHOICES)

    def __unicode__(self):
        return str(self.role)