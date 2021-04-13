from django.shortcuts import render
from django.http import JsonResponse
from App.models import *

from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlencode
from urllib.request import urlopen
import json
from datetime import datetime
import pandas as pd 
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
# Create your views here.

import logging
logger = logging.getLogger('testlogger')
@csrf_exempt
def submit(request):
    try:
        data=request.POST
        files=request.FILES
        remote_ip = request.META.get('HTTP_X_FORWARDED_FOR')

        print(data)
        logger.info(data)

        token=data.get('g-recaptcha-response')

        recaptcha_secret_key = '6LdheCUaAAAAANc0yQ4mcGKpfx7H4EBeS6i9Pk-u'

        URIReCaptcha = 'https://www.google.com/recaptcha/api/siteverify'
        params = urlencode({
            'secret': recaptcha_secret_key,
            'response': token,
            'remote_ip': remote_ip,
        })

        # print params
        d = urlopen(URIReCaptcha, params.encode('utf-8')).read()
        result = json.loads(d)
        success = result.get('success', None)
        print(success)
        
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
        now = datetime.now()
        print(now)
        # print(player1_name)
        if success==True:
            obj=FreeFire2(email=email,teamName=teamName,logo=logo,manager=manager,contact=contact,discord=discord,
            player1_name=player1_name,player1_email=player1_email,player1_contact=player1_contact,player1_IGN=player1_IGN,player1_UID=player1_UID,player1_photo=player1_photo,
            player2_name=player2_name,player2_email=player2_email,player2_contact=player2_contact,player2_IGN=player2_IGN,player2_UID=player2_UID,player2_photo=player2_photo,
            player3_name=player3_name,player3_email=player3_email,player3_contact=player3_contact,player3_IGN=player3_IGN,player3_UID=player3_UID,player3_photo=player3_photo,
            player4_name=player4_name,player4_email=player4_email,player4_contact=player4_contact,player4_IGN=player4_IGN,player4_UID=player4_UID,player4_photo=player4_photo,
            player5_name=player5_name,player5_email=player5_email,player5_contact=player5_contact,player5_IGN=player5_IGN,player5_UID=player5_UID,player5_photo=player5_photo,
            player6_name=player6_name,player6_email=player6_email,player6_contact=player6_contact,player6_IGN=player6_IGN,player6_UID=player6_UID,player6_photo=player6_photo
            )
            obj.save()
            n = str(int(random.random()*10000))+str(obj.id)
            obj.uniqueId=n

            obj.save()

            send_mail(
                'Esportz Invitational Series Free Fire Qualifier 2 Registration confirmation',
                '''Thank you for registering your team for the Second Free Fire qualifier of Esportz Premier Series! This mail is an official confirmation that we have recorded your entry. We will get in touch with you via phone or mail once your matches are scheduled. Please note that for the second qualifier we are accepting only 150 teams on a first come first serve basis. If you have not been shortlisted, please be assured that you will be given the first priority if you register for our 3rd qualifier which will be announced shortly. 
                \nYour unique registration id is: {}
                \nThis mail is auto-generated. For any queries, please get in touch with us on discord, facebook or Instagram.
                \nMake sure to follow us on insta, facebook discord and youtube for regular updates.
                \nhttps://linktr.ee/esportz.in
                '''.format(n),
                'tournamentbot@esportz.in',
                [obj.email],
                fail_silently=False,
            )
        
        print('done')
        return JsonResponse({
            'data':1
        })
    except Exception as e:
        logger.error(e)
        
        return JsonResponse({
            'data':0
        })
@login_required
@csrf_exempt
def excel(request):
    try:
        regs=FreeFire.objects.all()
        
        email=[]
        teamName=[]
        logo=[]
        manager=[]
        contact=[]
        discord=[]

        player1_name=[]
        player1_email=[]
        player1_contact=[]
        player1_IGN=[]
        player1_UID=[]
        player1_photo=[]
        
        player2_name=[]
        player2_email=[]
        player2_contact=[]
        player2_IGN=[]
        player2_UID=[]
        player2_photo=[]
        
        player3_name=[]
        player3_email=[]
        player3_contact=[]
        player3_IGN=[]
        player3_UID=[]
        player3_photo=[]
        
        player4_name=[]
        player4_email=[]
        player4_contact=[]
        player4_IGN=[]
        player4_UID=[]
        player4_photo=[]
        
        player5_name=[]
        player5_email=[]
        player5_contact=[]
        player5_IGN=[]
        player5_UID=[]
        player5_photo=[]
        
        player6_name=[]
        player6_email=[]
        player6_contact=[]
        player6_IGN=[]
        player6_UID=[]
        player6_photo=[]
        unique_id=[]

        for r in regs:
            email.append(r.email)
            teamName.append(r.teamName)
            logo.append(r.logo)
            manager.append(r.manager)
            contact.append(r.contact)
            discord.append(r.discord)
            
            player1_name.append(r.player1_name)
            player1_email.append(r.player1_email)
            player1_contact.append(r.player1_contact)
            player1_IGN.append(r.player1_IGN)
            player1_UID.append(r.player1_UID)
            player1_photo.append(r.player1_photo)
            
            player2_name.append(r.player2_name)
            player2_email.append(r.player2_email)
            player2_contact.append(r.player2_contact)
            player2_IGN.append(r.player2_IGN)
            player2_UID.append(r.player2_UID)
            player2_photo.append(r.player2_photo)
            
            player3_name.append(r.player3_name)
            player3_email.append(r.player3_email)
            player3_contact.append(r.player3_contact)
            player3_IGN.append(r.player3_IGN)
            player3_UID.append(r.player3_UID)
            player3_photo.append(r.player3_photo)
            
            player4_name.append(r.player4_name)
            player4_email.append(r.player4_email)
            player4_contact.append(r.player4_contact)
            player4_IGN.append(r.player4_IGN)
            player4_UID.append(r.player4_UID)
            player4_photo.append(r.player4_photo)
            
            player5_name.append(r.player5_name)
            player5_email.append(r.player5_email)
            player5_contact.append(r.player5_contact)
            player5_IGN.append(r.player5_IGN)
            player5_UID.append(r.player5_UID)
            player5_photo.append(r.player5_photo)
            
            player6_name.append(r.player6_name)
            player6_email.append(r.player6_email)
            player6_contact.append(r.player6_contact)
            player6_IGN.append(r.player6_IGN)
            player6_UID.append(r.player6_UID)
            player6_photo.append(r.player6_photo)
            unique_id.append(r.uniqueId)

        dataset = pd.DataFrame({'Email': email, 'Team Name':teamName,'Manager':manager,'Contact':contact,'Discord':discord,
        'Player 1 Name':player1_name,'Player 1 email':player1_email,'Player 1 contact':player1_contact,'Player 1 IGN':player1_IGN,'Player 1 UID':player1_UID,
        'Player 2 Name':player2_name,'Player 2 email':player2_email,'Player 2 contact':player2_contact,'Player 2 IGN':player2_IGN,'Player 2 UID':player2_UID,
        'Player 3 Name':player3_name,'Player 3 email':player3_email,'Player 3 contact':player3_contact,'Player 3 IGN':player3_IGN,'Player 3 UID':player3_UID,
        'Player 4 Name':player4_name,'Player 4 email':player4_email,'Player 4 contact':player4_contact,'Player 4 IGN':player4_IGN,'Player 4 UID':player4_UID,
        'Player 5 Name':player5_name,'Player 5 email':player5_email,'Player 5 contact':player5_contact,'Player 5 IGN':player5_IGN,'Player 5 UID':player5_UID,
        'Player 6 Name':player6_name,'Player 6 email':player6_email,'Player 6 contact':player6_contact,'Player 6 IGN':player6_IGN,'Player 6 UID':player6_UID,
        'unique_id':unique_id
        })
        dataset.to_excel ('file.xlsx', index = False, header=True)
        response = FileResponse(open('file.xlsx', 'rb'))
        return response
        
    except Exception as e:
        return JsonResponse({
            'error':str(e)
            })

@csrf_exempt
def fifa_submit(request):
    try:
        data=request.POST
        files=request.FILES
        remote_ip = request.META.get('HTTP_X_FORWARDED_FOR')

        print(data)
        logger.info(data)

        token=data.get('g-recaptcha-response')

        recaptcha_secret_key = '6LdheCUaAAAAANc0yQ4mcGKpfx7H4EBeS6i9Pk-u'

        URIReCaptcha = 'https://www.google.com/recaptcha/api/siteverify'
        params = urlencode({
            'secret': recaptcha_secret_key,
            'response': token,
            'remote_ip': remote_ip,
        })

        # print params
        d = urlopen(URIReCaptcha, params.encode('utf-8')).read()
        result = json.loads(d)
        success = result.get('success', None)
        print(success)
        
        email=data.get('email')
        name=data.get('name')
        photo=files.get('photo')
        psn=data.get('psn')
        contact=data.get('contact')
        discord=data.get('discord')
        ea=data.get('ea')
        age=data.get('age')
        ign=data.get('ign')
        webcam=data.get('webcam')

        now = datetime.now()
        print(now)
        if success==True:
            obj=Fifa(email=email,name=name,photo=photo,psn=psn,contact=contact,discord=discord,ea=ea,age=age,ign=ign,webcam=webcam)
            obj.save()
            n = str(int(random.random()*10000))+str(obj.id)
            obj.uniqueId=n

            obj.save()

            send_mail(
                'Esportz Premier Series Fifa Qualifier 1 Registration confirmation',
                '''Thank you for registering your team for the first Fifa qualifier of Esportz Premier Series! This mail is an official confirmation that we have recorded your entry. We will get in touch with you via phone or mail once your matches are scheduled. Please note that for the first qualifier we are accepting only 256 players on a first come first serve basis. If you have not been shortlisted, please be assured that you will be given the first priority if you register for our 2nd qualifier in July. 
                \nYour unique registration id is: {}
                \nThis mail is auto-generated. For any queries, please get in touch with us on discord, facebook or Instagram.
                \nMake sure to follow us on insta, facebook discord and youtube for regular updates.
                \nhttps://linktr.ee/esportz.in
                '''.format(n),
                'tournamentbot@esportz.in',
                [obj.email],
                fail_silently=False,
            )
        
        print('done')
        return JsonResponse({
            'data':1
        })
    except Exception as e:
        logger.error(e)
        
        return JsonResponse({
            'data':0
        })
@login_required
@csrf_exempt
def fifa_excel(request):
    try:
        regs=Fifa.objects.all()
        
        email=[]
        name=[]
        photo=[]
        psn=[]
        contact=[]
        discord=[]
        age=[]
        ea=[]
        ign=[]
        webcam=[]
        unique_id=[]
        for r in regs:
            email.append(r.email)
            name.append(r.name)
            photo.append(r.photo)
            contact.append(r.contact)
            discord.append(r.discord)
            psn.append(r.psn)
            ea.append(r.ea)
            age.append(r.age)
            ign.append(r.ign)
            webcam.append(r.webcam)
            unique_id.append(r.uniqueId)

        dataset = pd.DataFrame({'Email': email, 'Name':name,'Age':age,'Contact':contact,'Discord':discord,
        'PSn':psn,'IGN':ign,'EA':ea,'webcam':webcam,
        'unique_id':unique_id
        })
        dataset.to_excel ('file.xlsx', index = False, header=True)
        response = FileResponse(open('file.xlsx', 'rb'))
        return response
        
    except Exception as e:
        return JsonResponse({
            'error':str(e)
            })

    
@login_required
@csrf_exempt
def email(request):
    try:
        all_regs= FreeFire2.objects.all()
        for reg in all_regs:
            print(reg.uniqueId)
            if reg.uniqueId=='':
                n = str(int(random.random()*10000))+str(reg.id)
                reg.uniqueId=n
                reg.save()
                send_mail(
                    'Esportz Invitational Series Free Fire Qualifier 1 Registration confirmation',
                    '''Thank you for registering your team {} for the first Free Fire qualifier of Esportz Premier Series! This mail is an official confirmation that we have recorded your entry. We will get in touch with you via phone or mail once your matches are scheduled. Please note that for the first qualifier we are accepting only 150 teams on a first come first serve basis. If you have not been shortlisted, please be assured that you will be given the first priority if you register for our 2nd qualifier in March. 
                    \nYour unique registration id is: {}
                    \nThis mail is auto-generated. For any queries, please get in touch with us on discord, facebook or Instagram.
                    \nMake sure to follow us on insta, facebook discord and youtube for regular updates.
                    \nhttps://linktr.ee/esportz.in
                    '''.format(reg.teamName,n),
                    'tournamentbot@esportz.in',
                    # ['rushikesh@capitalgroup.me'],
                    [reg.email],
                    fail_silently=False,
                )
        return JsonResponse({
            'code':1
            })
    except Exception as e:
        return JsonResponse({
            'error':str(e)
            })


@csrf_exempt
def valo_submit(request):
    try:
        data=request.POST
        files=request.FILES
        remote_ip = request.META.get('HTTP_X_FORWARDED_FOR')

        print(data)
        logger.info(data)

        token=data.get('g-recaptcha-response')

        recaptcha_secret_key = '6LdheCUaAAAAANc0yQ4mcGKpfx7H4EBeS6i9Pk-u'

        URIReCaptcha = 'https://www.google.com/recaptcha/api/siteverify'
        params = urlencode({
            'secret': recaptcha_secret_key,
            'response': token,
            'remote_ip': remote_ip,
        })

        # print params
        d = urlopen(URIReCaptcha, params.encode('utf-8')).read()
        result = json.loads(d)
        success = result.get('success', None)
        print(success)
        
        email=data.get('email')
        teamName=data.get('teamName')
        logo=files.get('logo')
        contact=data.get('contact')

        player1_name=data.get('player1_name')
        player1_email=data.get('player1_email')
        player1_contact=data.get('player1_contact')
        player1_IGN=data.get('player1_IGN')
        # player1_riotID=data.get('player1_riotID')
        player1_discord=data.get('player1_discord')
        
        player2_name=data.get('player2_name')
        player2_email=data.get('player2_email')
        player2_contact=data.get('player2_contact')
        player2_IGN=data.get('player2_IGN')
        # player2_riotID=data.get('player2_riotID')
        player2_discord=data.get('player2_discord')
        
        player3_name=data.get('player3_name')
        player3_email=data.get('player3_email')
        player3_contact=data.get('player3_contact')
        player3_IGN=data.get('player3_IGN')
        # player3_riotID=data.get('player3_riotID')
        player3_discord=data.get('player3_discord')
        
        player4_name=data.get('player4_name')
        player4_email=data.get('player4_email')
        player4_contact=data.get('player4_contact')
        player4_IGN=data.get('player4_IGN')
        # player4_riotID=data.get('player4_riotID')
        player4_discord=data.get('player4_discord')
        


        player5_name=data.get('player5_name')
        player5_email=data.get('player5_email')
        player5_contact=data.get('player5_contact')
        player5_IGN=data.get('player5_IGN')
        # player5_riotID=data.get('player5_riotID')
        player5_discord=data.get('player5_discord')

        player6_IGN=data.get('player6_IGN')
        
        player7_IGN=data.get('player7_IGN')
        now = datetime.now()
        print(now)
        # print(player1_name)
        if success==True:
            obj=valorant(email=email,teamName=teamName,logo=logo,contact=contact,
            player1_name=player1_name,player1_email=player1_email,player1_contact=player1_contact,player1_IGN=player1_IGN,player1_discord=player1_discord,
            player2_name=player2_name,player2_email=player2_email,player2_contact=player2_contact,player2_IGN=player2_IGN,player2_discord=player2_discord,
            player3_name=player3_name,player3_email=player3_email,player3_contact=player3_contact,player3_IGN=player3_IGN,player3_discord=player3_discord,
            player4_name=player4_name,player4_email=player4_email,player4_contact=player4_contact,player4_IGN=player4_IGN,player4_discord=player4_discord,
            player5_name=player5_name,player5_email=player5_email,player5_contact=player5_contact,player5_IGN=player5_IGN,player5_discord=player5_discord,
            player6_IGN=player6_IGN,
            player7_IGN=player7_IGN
            )
            obj.save()
            n = str(int(random.random()*10000))+str(obj.id)
            obj.uniqueId=n

            obj.save()

            send_mail(
                'Esportz Premier Series Valorant Qualifier Registration confirmation',
                '''Thank you for registering your team for the First Valorant Qualifier of Esportz Premier Series! This mail is an official confirmation that we have recorded your entry. We will get in touch with you via phone or mail once your matches are scheduled. Please note that for the first qualifier we are accepting only 256 teams on a first come first serve basis. If you have not been shortlisted, please be assured that you will be given the first priority if you register for our 2nd qualifier which will be announced shortly. 
                \nYour unique registration id is: {}
                \nThis mail is auto-generated. For any queries, please get in touch with us on discord, facebook or Instagram.
                \nMake sure to follow us on insta, facebook discord and youtube for regular updates.
                \nhttps://linktr.ee/esportz.in
                '''.format(n),
                'tournamentbot@esportz.in',
                [obj.email],
                fail_silently=False,
            )
        
        print('done')
        return JsonResponse({
            'data':1
        })
    except Exception as e:
        logger.error(e)
        
        return JsonResponse({
            'data':0
        })

        
@login_required
@csrf_exempt
def valo_excel(request):
    try:
        regs=valorant.objects.all()
        
        email=[]
        teamName=[]
        logo=[]
        contact=[]

        player1_name=[]
        
        player1_email=[]
        player1_contact=[]
        player1_IGN=[]
        player1_riotID=[]
        player1_discord=[]
        
        player2_name=[]
        player2_email=[]
        player2_contact=[]
        player2_IGN=[]
        player2_riotID=[]
        player2_discord=[]
        
        player3_name=[]
        player3_email=[]
        player3_contact=[]
        player3_IGN=[]
        player3_riotID=[]
        player3_discord=[]
        
        player4_name=[]
        player4_email=[]
        player4_contact=[]
        player4_IGN=[]
        player4_riotID=[]
        player4_discord=[]
        
        
        player5_name=[]
        player5_email=[]
        player5_contact=[]
        player5_IGN=[]
        player5_riotID=[]
        player5_discord=[]

        player6_IGN=[]
        
        player7_IGN=[]
        unique_id=[]

        for r in regs:
            email.append(r.email)
            teamName.append(r.teamName)
            logo.append(r.logo)
            contact.append(r.contact)
            
            player1_name.append(r.player1_name)
            player1_email.append(r.player1_email)
            player1_contact.append(r.player1_contact)
            player1_IGN.append(r.player1_IGN)
            # player1_riotID.append(r.player1_riotID)
            player1_discord.append(r.player1_discord)
            
            player2_name.append(r.player2_name)
            player2_email.append(r.player2_email)
            player2_contact.append(r.player2_contact)
            player2_IGN.append(r.player2_IGN)
            # player2_riotID.append(r.player2_riotID)
            player2_discord.append(r.player2_discord)
            
            player3_name.append(r.player3_name)
            player3_email.append(r.player3_email)
            player3_contact.append(r.player3_contact)
            player3_IGN.append(r.player3_IGN)
            # player3_riotID.append(r.player3_riotID)
            player3_discord.append(r.player3_discord)
            
            player4_name.append(r.player4_name)
            player4_email.append(r.player4_email)
            player4_contact.append(r.player4_contact)
            player4_IGN.append(r.player4_IGN)
            # player4_riotID.append(r.player4_riotID)
            player4_discord.append(r.player4_discord)

            
            player5_name.append(r.player5_name)
            player5_email.append(r.player5_email)
            player5_contact.append(r.player5_contact)
            player5_IGN.append(r.player5_IGN)
            # player5_riotID.append(r.player5_riotID)
            player5_discord.append(r.player5_discord)
            
            player6_IGN.append(r.player6_IGN)
            
            player7_IGN.append(r.player7_IGN)
            unique_id.append(r.uniqueId)

        dataset = pd.DataFrame({'Email': email, 'Team Name':teamName,'Contact':contact,
        'Player 1 Name':player1_name,'Player 1 email':player1_email,'Player 1 contact':player1_contact,'Player 1 IGN':player1_IGN,
        'Player 2 Name':player2_name,'Player 2 email':player2_email,'Player 2 contact':player2_contact,'Player 2 IGN':player2_IGN,
        'Player 3 Name':player3_name,'Player 3 email':player3_email,'Player 3 contact':player3_contact,'Player 3 IGN':player3_IGN,
        'Player 4 Name':player4_name,'Player 4 email':player4_email,'Player 4 contact':player4_contact,'Player 4 IGN':player4_IGN,
        'Player 5 Name':player5_name,'Player 5 email':player5_email,'Player 5 contact':player5_contact,'Player 5 IGN':player5_IGN,
        'Substitute 1 IGN':player6_IGN,
        'Substitute 2 IGN':player7_IGN,
        'unique_id':unique_id
        })
        dataset.to_excel ('file.xlsx', index = False, header=True)
        response = FileResponse(open('file.xlsx', 'rb'))
        return response
        
    except Exception as e:
        return JsonResponse({
            'error':str(e)
            })