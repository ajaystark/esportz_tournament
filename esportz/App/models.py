from django.db import models
from django.contrib import admin
from django import forms
from django.forms import ModelForm, Textarea
from datetime import datetime

def get_upload_path(instance,filename):
    name='images/ffwildcard/{0}/{1}'.format(instance.teamName, filename)
    print(name)
    return name
    
def get_upload_path_player(instance,filename):
    name='images/fifawilcard/{0}/{1}'.format(instance.name, filename)
    return name


def get_upload_path_valo2(instance,filename):
    name='images/valo4/{0}/{1}'.format(instance.teamName, filename)
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



class FreeFire3(models.Model):
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
        verbose_name = 'Free Fire 3 Reg'


class FreeFireAdmin(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord','logo','uniqueId')

class FreeFireAdmin3(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord','logo','uniqueId')



class FreeFire4(models.Model):
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
        verbose_name = 'Free Fire 4 Reg'
        
class FreeFireAdmin4(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord','logo','uniqueId')
        
class FreeFireWilcard(models.Model):
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
        verbose_name = 'Free Fire Wilcard'

class FreeFireAdminWilcard(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord','logo','uniqueId')



class FreeFire2(models.Model):
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
        verbose_name = 'Free Fire 2 Reg'


class FreeFireAdmin2(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact', 'discord','logo','uniqueId')

class Fifa(models.Model):
    email= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_upload_path_player, blank=True)
    contact= models.CharField(max_length=50)
    discord= models.CharField(max_length=50)
    psn= models.CharField(max_length=50)
    ea= models.CharField(max_length=50)
    age= models.IntegerField(blank=True)
    ign= models.CharField(max_length=50)
    webcam= models.CharField(max_length=50)
    uniqueId= models.CharField(max_length=50, blank=True)

    class Meta:  
        verbose_name = 'Fifa Reg'
class FifaAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'contact', 'discord','photo','uniqueId')
    
class Fifa2(models.Model):
    email= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_upload_path_player, blank=True)
    contact= models.CharField(max_length=50)
    discord= models.CharField(max_length=50)
    psn= models.CharField(max_length=50)
    ea= models.CharField(max_length=50)
    age= models.IntegerField(blank=True)
    ign= models.CharField(max_length=50)
    webcam= models.CharField(max_length=50)
    uniqueId= models.CharField(max_length=50, blank=True)

    class Meta:  
        verbose_name = 'Fifa 2 Reg'
class FifaAdmin2(admin.ModelAdmin):
    list_display = ('email', 'name', 'contact', 'discord','photo','uniqueId')
    
    
class FifaWildcard(models.Model):
    email= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_upload_path_player, blank=True)
    contact= models.CharField(max_length=50)
    discord= models.CharField(max_length=50)
    psn= models.CharField(max_length=50)
    ea= models.CharField(max_length=50)
    age= models.IntegerField(blank=True)
    ign= models.CharField(max_length=50)
    webcam= models.CharField(max_length=50)
    uniqueId= models.CharField(max_length=50, blank=True)

    class Meta:  
        verbose_name = 'Fifa Wildcard'
class FifaAdminWildcard(admin.ModelAdmin):
    list_display = ('email', 'name', 'contact', 'discord','photo','uniqueId')


class valorant(models.Model):
    email= models.CharField(max_length=50)
    teamName= models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_upload_path_valo2, blank=True)
    contact= models.CharField(max_length=50)

    player1_name= models.CharField(max_length=50, blank=True)
    player1_email= models.CharField(max_length=50, blank=True)
    player1_contact= models.CharField(max_length=50, blank=True)
    player1_IGN= models.CharField(max_length=50, blank=True)
    # player1_riotID= models.CharField(max_length=50, blank=True)
    player1_discord = models.CharField(max_length=50, blank=True)

    
    player2_name= models.CharField(max_length=50, blank=True)
    player2_email= models.CharField(max_length=50, blank=True)
    player2_contact= models.CharField(max_length=50, blank=True)
    player2_IGN= models.CharField(max_length=50, blank=True)
    # player2_riotID= models.CharField(max_length=50, blank=True)
    player2_discord = models.CharField(max_length=50, blank=True)
    
    player3_name= models.CharField(max_length=50, blank=True)
    player3_email= models.CharField(max_length=50, blank=True)
    player3_contact= models.CharField(max_length=50, blank=True)
    player3_IGN= models.CharField(max_length=50, blank=True)
    # player3_riotID= models.CharField(max_length=50, blank=True)
    player3_discord = models.CharField(max_length=50, blank=True)
    
    player4_name= models.CharField(max_length=50, blank=True)
    player4_email= models.CharField(max_length=50, blank=True)
    player4_contact= models.CharField(max_length=50, blank=True)
    player4_IGN= models.CharField(max_length=50, blank=True)
    # player4_riotID= models.CharField(max_length=50, blank=True)
    player4_discord = models.CharField(max_length=50, blank=True)

    
    player5_name= models.CharField(max_length=50, blank=True)
    player5_email= models.CharField(max_length=50, blank=True)
    player5_contact= models.CharField(max_length=50, blank=True)
    player5_IGN= models.CharField(max_length=50, blank=True)
    # player5_riotID= models.CharField(max_length=50, blank=True)
    player5_discord = models.CharField(max_length=50, blank=True)
    
    player6_IGN= models.CharField(max_length=50, blank=True)
    
    player7_IGN= models.CharField(max_length=50, blank=True)
    uniqueId= models.CharField(max_length=50, blank=True)   

    # time = models.DateTimeField(default=datetime.now, blank=True) 

    class Meta:  
        verbose_name = 'Valorant Reg'


class valorantAdmin(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact','logo','uniqueId')



class valorant2(models.Model):
    email= models.CharField(max_length=50)
    teamName= models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_upload_path_valo2, blank=True)
    contact= models.CharField(max_length=50)

    player1_name= models.CharField(max_length=50, blank=True)
    player1_email= models.CharField(max_length=50, blank=True)
    player1_contact= models.CharField(max_length=50, blank=True)
    player1_IGN= models.CharField(max_length=50, blank=True)
    # player1_riotID= models.CharField(max_length=50, blank=True)
    player1_discord = models.CharField(max_length=50, blank=True)

    
    player2_name= models.CharField(max_length=50, blank=True)
    player2_email= models.CharField(max_length=50, blank=True)
    player2_contact= models.CharField(max_length=50, blank=True)
    player2_IGN= models.CharField(max_length=50, blank=True)
    # player2_riotID= models.CharField(max_length=50, blank=True)
    player2_discord = models.CharField(max_length=50, blank=True)
    
    player3_name= models.CharField(max_length=50, blank=True)
    player3_email= models.CharField(max_length=50, blank=True)
    player3_contact= models.CharField(max_length=50, blank=True)
    player3_IGN= models.CharField(max_length=50, blank=True)
    # player3_riotID= models.CharField(max_length=50, blank=True)
    player3_discord = models.CharField(max_length=50, blank=True)
    
    player4_name= models.CharField(max_length=50, blank=True)
    player4_email= models.CharField(max_length=50, blank=True)
    player4_contact= models.CharField(max_length=50, blank=True)
    player4_IGN= models.CharField(max_length=50, blank=True)
    # player4_riotID= models.CharField(max_length=50, blank=True)
    player4_discord = models.CharField(max_length=50, blank=True)

    
    player5_name= models.CharField(max_length=50, blank=True)
    player5_email= models.CharField(max_length=50, blank=True)
    player5_contact= models.CharField(max_length=50, blank=True)
    player5_IGN= models.CharField(max_length=50, blank=True)
    # player5_riotID= models.CharField(max_length=50, blank=True)
    player5_discord = models.CharField(max_length=50, blank=True)
    
    player6_IGN= models.CharField(max_length=50, blank=True)
    
    player7_IGN= models.CharField(max_length=50, blank=True)
    uniqueId= models.CharField(max_length=50, blank=True)   

    # time = models.DateTimeField(default=datetime.now, blank=True) 

    class Meta:  
        verbose_name = 'Valorant 2 Reg'


class valorantAdmin2(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact','logo','uniqueId')


class valorant3(models.Model):
    email= models.CharField(max_length=50)
    teamName= models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_upload_path_valo2, blank=True)
    contact= models.CharField(max_length=50)

    player1_name= models.CharField(max_length=50, blank=True)
    player1_email= models.CharField(max_length=50, blank=True)
    player1_contact= models.CharField(max_length=50, blank=True)
    player1_IGN= models.CharField(max_length=50, blank=True)
    # player1_riotID= models.CharField(max_length=50, blank=True)
    player1_discord = models.CharField(max_length=50, blank=True)

    
    player2_name= models.CharField(max_length=50, blank=True)
    player2_email= models.CharField(max_length=50, blank=True)
    player2_contact= models.CharField(max_length=50, blank=True)
    player2_IGN= models.CharField(max_length=50, blank=True)
    # player2_riotID= models.CharField(max_length=50, blank=True)
    player2_discord = models.CharField(max_length=50, blank=True)
    
    player3_name= models.CharField(max_length=50, blank=True)
    player3_email= models.CharField(max_length=50, blank=True)
    player3_contact= models.CharField(max_length=50, blank=True)
    player3_IGN= models.CharField(max_length=50, blank=True)
    # player3_riotID= models.CharField(max_length=50, blank=True)
    player3_discord = models.CharField(max_length=50, blank=True)
    
    player4_name= models.CharField(max_length=50, blank=True)
    player4_email= models.CharField(max_length=50, blank=True)
    player4_contact= models.CharField(max_length=50, blank=True)
    player4_IGN= models.CharField(max_length=50, blank=True)
    # player4_riotID= models.CharField(max_length=50, blank=True)
    player4_discord = models.CharField(max_length=50, blank=True)

    
    player5_name= models.CharField(max_length=50, blank=True)
    player5_email= models.CharField(max_length=50, blank=True)
    player5_contact= models.CharField(max_length=50, blank=True)
    player5_IGN= models.CharField(max_length=50, blank=True)
    # player5_riotID= models.CharField(max_length=50, blank=True)
    player5_discord = models.CharField(max_length=50, blank=True)
    
    player6_IGN= models.CharField(max_length=50, blank=True)
    
    player7_IGN= models.CharField(max_length=50, blank=True)
    uniqueId= models.CharField(max_length=50, blank=True)   

    # time = models.DateTimeField(default=datetime.now, blank=True) 

    class Meta:  
        verbose_name = 'Valorant 3 Reg'


class valorantAdmin3(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact','logo','uniqueId')
    
class valorant4(models.Model):
    email= models.CharField(max_length=50)
    teamName= models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_upload_path_valo2, blank=True)
    contact= models.CharField(max_length=50)

    player1_name= models.CharField(max_length=50, blank=True)
    player1_email= models.CharField(max_length=50, blank=True)
    player1_contact= models.CharField(max_length=50, blank=True)
    player1_IGN= models.CharField(max_length=50, blank=True)
    # player1_riotID= models.CharField(max_length=50, blank=True)
    player1_discord = models.CharField(max_length=50, blank=True)

    
    player2_name= models.CharField(max_length=50, blank=True)
    player2_email= models.CharField(max_length=50, blank=True)
    player2_contact= models.CharField(max_length=50, blank=True)
    player2_IGN= models.CharField(max_length=50, blank=True)
    # player2_riotID= models.CharField(max_length=50, blank=True)
    player2_discord = models.CharField(max_length=50, blank=True)
    
    player3_name= models.CharField(max_length=50, blank=True)
    player3_email= models.CharField(max_length=50, blank=True)
    player3_contact= models.CharField(max_length=50, blank=True)
    player3_IGN= models.CharField(max_length=50, blank=True)
    # player3_riotID= models.CharField(max_length=50, blank=True)
    player3_discord = models.CharField(max_length=50, blank=True)
    
    player4_name= models.CharField(max_length=50, blank=True)
    player4_email= models.CharField(max_length=50, blank=True)
    player4_contact= models.CharField(max_length=50, blank=True)
    player4_IGN= models.CharField(max_length=50, blank=True)
    # player4_riotID= models.CharField(max_length=50, blank=True)
    player4_discord = models.CharField(max_length=50, blank=True)

    
    player5_name= models.CharField(max_length=50, blank=True)
    player5_email= models.CharField(max_length=50, blank=True)
    player5_contact= models.CharField(max_length=50, blank=True)
    player5_IGN= models.CharField(max_length=50, blank=True)
    # player5_riotID= models.CharField(max_length=50, blank=True)
    player5_discord = models.CharField(max_length=50, blank=True)
    
    player6_IGN= models.CharField(max_length=50, blank=True)
    
    player7_IGN= models.CharField(max_length=50, blank=True)
    uniqueId= models.CharField(max_length=50, blank=True)   

    # time = models.DateTimeField(default=datetime.now, blank=True) 

    class Meta:  
        verbose_name = 'Valorant 4 Reg'


class valorantAdmin4(admin.ModelAdmin):
    list_display = ('email', 'teamName', 'contact','logo','uniqueId')
    
admin.site.register(FreeFire, FreeFireAdmin)
admin.site.register(FreeFire2, FreeFireAdmin2)
admin.site.register(FreeFire3, FreeFireAdmin3)
admin.site.register(FreeFire4, FreeFireAdmin4)
admin.site.register(FreeFireWilcard, FreeFireAdminWilcard)
admin.site.register(valorant, valorantAdmin)
admin.site.register(valorant2, valorantAdmin2)
admin.site.register(valorant3, valorantAdmin3)
admin.site.register(valorant4, valorantAdmin4)
admin.site.register(Fifa, FifaAdmin)
admin.site.register(Fifa2, FifaAdmin2)
admin.site.register(FifaWildcard, FifaAdminWildcard)