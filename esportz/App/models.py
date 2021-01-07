from django.db import models
from django.contrib import admin
from django import forms
from django.forms import ModelForm, Textarea

class FreeFire(models.Model):
    email= models.CharField(max_length=50)
    teamName= models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images', blank=True)
    manager= models.CharField(max_length=50)
    contact= models.CharField(max_length=50)
    discord= models.CharField(max_length=50)

    player1name= models.CharField(max_length=50, blank=True)
    player1email= models.CharField(max_length=50, blank=True)
    player1contact= models.CharField(max_length=50, blank=True)
    player1IGN= models.CharField(max_length=50, blank=True)
    player1UID= models.CharField(max_length=50, blank=True)
    player1photo = models.ImageField(upload_to='images', blank=True)

    
    player2name= models.CharField(max_length=50, blank=True)
    player2email= models.CharField(max_length=50, blank=True)
    player2contact= models.CharField(max_length=50, blank=True)
    player2IGN= models.CharField(max_length=50, blank=True)
    player2UID= models.CharField(max_length=50, blank=True)
    player2photo = models.ImageField(upload_to='images', blank=True)
    
    player3name= models.CharField(max_length=50, blank=True)
    player3email= models.CharField(max_length=50, blank=True)
    player3contact= models.CharField(max_length=50, blank=True)
    player3IGN= models.CharField(max_length=50, blank=True)
    player3UID= models.CharField(max_length=50, blank=True)
    player3photo = models.ImageField(upload_to='images', blank=True)
    
    player4name= models.CharField(max_length=50, blank=True)
    player4email= models.CharField(max_length=50, blank=True)
    player4contact= models.CharField(max_length=50, blank=True)
    player4IGN= models.CharField(max_length=50, blank=True)
    player4UID= models.CharField(max_length=50, blank=True)
    player4photo = models.ImageField(upload_to='images', blank=True)
    
    player5name= models.CharField(max_length=50, blank=True)
    player5email= models.CharField(max_length=50, blank=True)
    player5contact= models.CharField(max_length=50, blank=True)
    player5IGN= models.CharField(max_length=50, blank=True)
    player5UID= models.CharField(max_length=50, blank=True)
    player5photo = models.ImageField(upload_to='images', blank=True)
    
    player6name= models.CharField(max_length=50, blank=True)
    player6email= models.CharField(max_length=50, blank=True)
    player6contact= models.CharField(max_length=50, blank=True)
    player6IGN= models.CharField(max_length=50, blank=True)
    player6UID= models.CharField(max_length=50, blank=True)
    player6photo = models.ImageField(upload_to='images', blank=True)

    


    class Meta:  
        verbose_name = 'Free Fire Reg'


class FreeFireAdmin(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord')



admin.site.register(FreeFire, FreeFireAdmin)