from django.db import models
from django.contrib import admin
from django import forms
from django.forms import ModelForm, Textarea
from datetime import datetime

def get_upload_path(instance,filename):
    name='images/{0}/{1}'.format(instance.teamName, filename)
    print(name)
    return name
class FreeFire(models.Model):
    email= models.CharField(max_length=50)
    teamName= models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_upload_path, blank=True)
    manager= models.CharField(max_length=50)
    contact= models.CharField(max_length=50)
    discord= models.CharField(max_length=50)

    player1_name= models.CharField(max_length=50, blank=True)
    player1_email= models.CharField(max_length=50, blank=True)
    player1_contact= models.CharField(max_length=50, blank=True)
    player1_IGN= models.CharField(max_length=50, blank=True)
    player1_UID= models.CharField(max_length=50, blank=True)
    player1_photo = models.ImageField(upload_to=get_upload_path, blank=True)

    
    player2_name= models.CharField(max_length=50, blank=True)
    player2_email= models.CharField(max_length=50, blank=True)
    player2_contact= models.CharField(max_length=50, blank=True)
    player2_IGN= models.CharField(max_length=50, blank=True)
    player2_UID= models.CharField(max_length=50, blank=True)
    player2_photo = models.ImageField(upload_to=get_upload_path, blank=True)
    
    player3_name= models.CharField(max_length=50, blank=True)
    player3_email= models.CharField(max_length=50, blank=True)
    player3_contact= models.CharField(max_length=50, blank=True)
    player3_IGN= models.CharField(max_length=50, blank=True)
    player3_UID= models.CharField(max_length=50, blank=True)
    player3_photo = models.ImageField(upload_to=get_upload_path, blank=True)
    
    player4_name= models.CharField(max_length=50, blank=True)
    player4_email= models.CharField(max_length=50, blank=True)
    player4_contact= models.CharField(max_length=50, blank=True)
    player4_IGN= models.CharField(max_length=50, blank=True)
    player4_UID= models.CharField(max_length=50, blank=True)
    player4_photo = models.ImageField(upload_to=get_upload_path, blank=True)
    
    player5_name= models.CharField(max_length=50, blank=True)
    player5_email= models.CharField(max_length=50, blank=True)
    player5_contact= models.CharField(max_length=50, blank=True)
    player5_IGN= models.CharField(max_length=50, blank=True)
    player5_UID= models.CharField(max_length=50, blank=True)
    player5_photo = models.ImageField(upload_to=get_upload_path, blank=True)
    
    player6_name= models.CharField(max_length=50, blank=True)
    player6_email= models.CharField(max_length=50, blank=True)
    player6_contact= models.CharField(max_length=50, blank=True)
    player6_IGN= models.CharField(max_length=50, blank=True)
    player6_UID= models.CharField(max_length=50, blank=True)
    player6_photo = models.ImageField(upload_to=get_upload_path, blank=True)
    uniqueId= models.CharField(max_length=50, blank=True)

    # time = models.DateTimeField(default=datetime.now, blank=True) 

    class Meta:  
        verbose_name = 'Free Fire Reg'


class FreeFireAdmin(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord','logo','uniqueId')


admin.site.register(FreeFire, FreeFireAdmin)