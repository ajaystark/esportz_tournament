from django.shortcuts import render
from django.http import JsonResponse
from App.models import *

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def submit(request):
    data=request.POST
    files=request.FILES

    print(files)
    
    email=data.get('email')
    teamName=data.get('teamName')
    logo=files.get('logo')
    manager=data.get('manager')
    contact=data.get('contact')
    discord=data.get('discord')

    player1_name=data.get('player1_name')
    player1_email=data.get('player1_email')
    player1_contact=data.get('player1_contact')
    player1_IGN=data.get('player1_IGN')
    player1_UID=data.get('player1_UID')
    player1_photo=files.get('player1_photo')
    
    player2_name=data.get('player2_name')
    player2_email=data.get('player2_email')
    player2_contact=data.get('player2_contact')
    player2_IGN=data.get('player2_IGN')
    player2_UID=data.get('player2_UID')
    player2_photo=files.get('player2_photo')
    
    player3_name=data.get('player3_name')
    player3_email=data.get('player3_email')
    player3_contact=data.get('player3_contact')
    player3_IGN=data.get('player3_IGN')
    player3_UID=data.get('player3_UID')
    player3_photo=files.get('player3_photo')
    
    player4_name=data.get('player4_name')
    player4_email=data.get('player4_email')
    player4_contact=data.get('player4_contact')
    player4_IGN=data.get('player4_IGN')
    player4_UID=data.get('player4_UID')
    player4_photo=files.get('player4_photo')
    
    player5_name=data.get('player5_name')
    player5_email=data.get('player5_email')
    player5_contact=data.get('player5_contact')
    player5_IGN=data.get('player5_IGN')
    player5_UID=data.get('player5_UID')
    player5_photo=files.get('player5_photo')
    
    player6_name=data.get('player6_name')
    player6_email=data.get('player6_email')
    player6_contact=data.get('player6_contact')
    player6_IGN=data.get('player6_IGN')
    player6_UID=data.get('player6_UID')
    player6_photo=files.get('player6_photo')

    # print(player1_name)

    obj=FreeFire(email=email,teamName=teamName,logo=logo,manager=manager,contact=contact,discord=discord,
    player1_name=player1_name,player1_email=player1_email,player1_contact=player1_contact,player1_IGN=player1_IGN,player1_UID=player1_UID,player1_photo=player1_photo,
    player2_name=player2_name,player2_email=player2_email,player2_contact=player2_contact,player2_IGN=player2_IGN,player2_UID=player2_UID,player2_photo=player2_photo,
    player3_name=player3_name,player3_email=player3_email,player3_contact=player3_contact,player3_IGN=player3_IGN,player3_UID=player3_UID,player3_photo=player3_photo,
    player4_name=player4_name,player4_email=player4_email,player4_contact=player4_contact,player4_IGN=player4_IGN,player4_UID=player4_UID,player4_photo=player4_photo,
    player5_name=player5_name,player5_email=player5_email,player5_contact=player5_contact,player5_IGN=player5_IGN,player5_UID=player5_UID,player5_photo=player5_photo,
    player6_name=player6_name,player6_email=player6_email,player6_contact=player6_contact,player6_IGN=player6_IGN,player6_UID=player6_UID,player6_photo=player6_photo,
    )
    obj.save()
    
    print('done')
    return JsonResponse({
        'data':1
    })