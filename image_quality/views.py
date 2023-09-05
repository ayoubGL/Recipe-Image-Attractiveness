from select import select
from django.forms import formset_factory
from django.db.models import Count
# import datetime
from datetime import datetime 
import pandas as pd
from random import choice, sample
import random
from sys import prefix
from django import forms
from django.db import reset_queries
from django.forms.models import ModelForm
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from pandas.core.indexes import category
import itertools
from .forms import Personal_infoForm, SaladRatingForm, PastaRatingForm, DissertRatingForm, SnacksRatingForm, recipesRatingForm, Ghs_fkForm

from .models import  Personal_info,  Salad, Snacks, Pasta, Dissert, PastaRating, DissertRating, SnacksRating, SaladRating, recipes, recipesRating, Ghs_fk
# from .app import *
# Create your views here.
# person_id = 0
import string
import random
import re
from django.core.cache import cache
# Create your views here.


def home(request):
    request.session['person_id'] = 0
    
    # views = ["rate_sate", "rate_paste","rate_snacks","rate_dissert"]
    # shuffle`views`
    # index = 0 // 0-3
    # views[index]
    #prolific_id = , msg)
    #prolific_id = str(prolific_id.group(1))
    full_url = request.get_full_path()
    #request.GET['PROLIFIC_PID']
    # print('Full',request.get_full_path())
    #print(full_url)
    if 'PROLIFIC_PID' in full_url:
        prolific_id = re.search("PROLIFIC_PID=(.*?)&STUDY_ID",full_url)
        request.session['prolific_id'] = str(prolific_id.group(1))
        #print("----------",prolific_id.group(1))
    else:
        request.session['prolific_id'] = '000'
    return render(request, 'image_quality/homes.html')

        # index++
        
def personal_info(request):
    user_selected = Personal_info.objects.filter(id = request.session['person_id'])
    if user_selected:
        Personal_info.objects.filter(id=request.session['person_id']).delete()
    if request.method == 'POST':
        personl_info = Personal_infoForm(request.POST)
        if personl_info.is_valid():
            answer = personl_info.save(commit=False)
            
            rd_str =''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            time_now = datetime.now().strftime('%H%M%S')
            gene_session = 'dars'+time_now +'_'+str(answer.id)+rd_str
            personl_info.instance.session_id = gene_session

            answer = personl_info.save(commit=True)
            
            request.session['person_id'] = answer.id
            gene_session = 'dars'+time_now +'_'+str(answer.id)+rd_str
            personl_info.instance.session_id = request.session['prolific_id']
            
            request.session['session_id'] = gene_session
            answer = personl_info.save(commit=True)
            request.session['n'] = 0

            request.session['person_id'] = answer.id
            # return redirect('image_quality:rate_salad')
            return redirect('image_quality:ghs_fk')
    else:
        personl_info = Personal_infoForm()
    return render(request, 'image_quality/personal_info.html', context={'form': personl_info})


def ghs_fk(request):
    user_selected = Ghs_fk.objects.filter(id = request.session['person_id'])
    if user_selected:
        ghs_fk.objects.filter(id=request.session['person_id']).delete()
    if request.method == 'POST':
        ghs_fk_form = Ghs_fkForm(request.POST)
        #print('------- Here')
        if ghs_fk_form.is_valid():
            answer = ghs_fk_form.save(commit=False)

            rd_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            time_now = datetime.now().strftime('%H%M%S')
            gene_session = 'dars' +  time_now + '_' + str(answer.id) + rd_str
            ghs_fk_form.instance.session_id = gene_session
            ghs_fk_form.instance.person_id = request.session['person_id']
            #print(';;;;;;;;;;;here')
            answer = ghs_fk_form.save(commit = True)

            #request.session['person_id'] = answer.id
            return redirect('image_quality:rate_recipes')
        else:
            print('not valid')
    else:
        ghs_fk_form = Ghs_fkForm()
    return render(request, 'image_quality/Personal_knowledge.html', context={'form':ghs_fk_form})






def rate_salad(request):
    user_selected  = SaladRating.objects.filter(person_id= request.session['person_id'])
    if user_selected:
        SaladRating.objects.filter(person_id= request.session['person_id']).delete()
    # S = Salad.objects.all()
    rated_ones = SaladRating.objects.all()
    
    
    notRated =  Salad.objects.exclude(id__in=rated_ones.values('salad'))
    S = notRated
    # print(len(S))
    
    # if rated_ones is S:
    #     print(rated_ones,"----------->")
    # else:
    #     print(rated_ones.values('salad'))
        
    if request.method == "POST":    
        S1 = SaladRatingForm(request.POST, prefix='S1')
        
        S2 = SaladRatingForm(request.POST,prefix='S2')
        S3 = SaladRatingForm(request.POST,prefix='S3')
        S4 = SaladRatingForm(request.POST,prefix='S4')
        S5 = SaladRatingForm(request.POST,prefix='S5')
        S6 = SaladRatingForm(request.POST,prefix='S6')
        S7 = SaladRatingForm(request.POST,prefix='S7')
        S8 = SaladRatingForm(request.POST,prefix='S8')
        S9 = SaladRatingForm(request.POST,prefix='S9')
        S10 = SaladRatingForm(request.POST,prefix='S10')
        
        # if S1.is_valid():
        #     print('------------',S1.cleaned_data.get('rating'))
        # else:
        #     print('-----ELSE-------',S1.cleaned_data.get('rating'))
        #     print('----------', S[0].id)
        
        S_r1 = SaladRating()
        S_r2 = SaladRating()
        S_r3 = SaladRating()
        S_r4 = SaladRating()
        S_r5 = SaladRating()
        S_r6 = SaladRating()
        S_r7 = SaladRating()
        S_r8 = SaladRating()
        S_r9 = SaladRating()
        S_r10 = SaladRating()
        
        print('------------',S2.is_valid())
        
        if S1.is_valid() and S2.is_valid() and S3.is_valid() and S4.is_valid() and  S5.is_valid() and S6.is_valid() and S7.is_valid() and S8.is_valid() and S9.is_valid() and S10.is_valid() :
            person = Personal_info.objects.get(id=request.session['person_id'])
        
            S_r1.person = S_r2.person =S_r3.person=S_r4.person=S_r5.person=S_r6.person=S_r7.person=S_r8.person=S_r2.person=S_r9.person=S_r10.person = person
                
            S_r1.salad_id = S[0].id
            S_r1.rating = S1.cleaned_data.get('rating')
            S_r1.judging = S1.cleaned_data.get('judging')
            print('-----Ratings--',S_r1.judging )
            S_r1.save()
            
            S_r2.salad_id = S[1].id
            S_r2.rating = S2.cleaned_data.get('rating')
            S_r2.judging = S2.cleaned_data.get('judging')
            S_r2.save()       
                    
            S_r3.salad_id = S[2].id
            S_r3.rating = S3.cleaned_data.get('rating')
            S_r3.judging = S3.cleaned_data.get('judging')
            S_r3.save()
            
            
            S_r4.salad_id = S[3].id
            S_r4.rating = S4.cleaned_data.get('rating')
            S_r4.judging = S4.cleaned_data.get('judging')
            S_r4.save()
                    
            S_r5.salad_id = S[4].id
            S_r5.rating = S5.cleaned_data.get('rating')
            S_r5.judging = S5.cleaned_data.get('judging')
            S_r5.save()

            S_r6.salad_id = S[5].id
            S_r6.rating = S6.cleaned_data.get('rating')
            S_r6.judging = S6.cleaned_data.get('judging')
            S_r6.save()
            
            S_r7.salad_id = S[6].id
            S_r7.rating = S7.cleaned_data.get('rating')
            S_r7.judging = S7.cleaned_data.get('judging')
            S_r7.save()
            
            S_r8.salad_id = S[7].id
            S_r8.rating = S8.cleaned_data.get('rating')
            S_r8.judging = S8.cleaned_data.get('judging')
            S_r8.save()
            
            S_r9.salad_id = S[8].id
            S_r9.rating = S9.cleaned_data.get('rating')
            S_r9.judging = S9.cleaned_data.get('judging')
            S_r9.save()
            
            
            S_r10.salad_id = S[9].id
            S_r10.rating = S10.cleaned_data.get('rating')
            S_r10.judging = S10.cleaned_data.get('judging')
            S_r10.save()
            return redirect('image_quality:rate_pasta')
        else: 
            print('not valid')
    else:
       
        S1 = SaladRatingForm(prefix='S1')
        S2 = SaladRatingForm(prefix='S2')
        S3 = SaladRatingForm(prefix='S3')
        S4 = SaladRatingForm(prefix='S4')
        S5 = SaladRatingForm(prefix='S5')
        S6 = SaladRatingForm(prefix='S6')
        S7 = SaladRatingForm(prefix='S7')
        S8 = SaladRatingForm(prefix='S8')
        S9 = SaladRatingForm(prefix='S9')
        S10 = SaladRatingForm(prefix='S10')
    context ={
                        'S1_F': S1,  's_1':S[0],
                        'S2_F':S2,  's_2':S[1],
                        'S3_F':S3, 's_3':S[2],
                        'S4_F':S4, 's_4':S[3],
                        'S5_F':S5, 's_5':S[4],
                        
                        'S6_F': S6,  's_6':S[5],
                        'S7_F':S7,  's_7':S[6],
                        'S8_F':S8, 's_8':S[7],
                        'S9_F':S9, 's_9':S[8],
                        'S10_F':S10, 's_10':S[9],

    }
  
      
  
    return render(request, 'image_quality/rate_salad.html', context)

def rate_pasta(request):
    user_selected  = PastaRating.objects.filter(person_id= request.session['person_id'])
    if user_selected:
        PastaRating.objects.filter(person_id= request.session['person_id']).delete()
    
    
    rated_ones = PastaRating.objects.all()
    
    
    notRated =  Pasta.objects.exclude(id__in=rated_ones.values('pasta'))
    P = notRated
    print('---',P)
    if request.method == "POST":    
        P1 =PastaRatingForm(request.POST, prefix='S1')
        
        P2 =PastaRatingForm(request.POST,prefix='S2')
        P3 =PastaRatingForm(request.POST,prefix='S3')
        P4 =PastaRatingForm(request.POST,prefix='S4')
        P5 =PastaRatingForm(request.POST,prefix='S5')
        P6 =PastaRatingForm(request.POST,prefix='S6')
        P7 =PastaRatingForm(request.POST,prefix='S7')
        P8 =PastaRatingForm(request.POST,prefix='S8')
        P9 =PastaRatingForm(request.POST,prefix='S9')
        P10 =PastaRatingForm(request.POST,prefix='S10')
        
        # if P1.is_valid():
        #     print('------------',P1.cleaned_data.get('rating'))
        # else:
        #     print('-----ELSE-------',P1.cleaned_data.get('rating'))
        #     print('----------', P[0].id)
        
        P_r1 = PastaRating()
        P_r2 = PastaRating()
        P_r3 = PastaRating()
        P_r4 = PastaRating()
        P_r5 = PastaRating()
        P_r6 = PastaRating()
        P_r7 = PastaRating()
        P_r8 = PastaRating()
        P_r9 = PastaRating()
        P_r10 = PastaRating()
            
        # print('------------',S1.cleaned_data.get('rating'))
        
        if P1.is_valid() and P2.is_valid() and P3.is_valid() and P4.is_valid() and  P5.is_valid() and P6.is_valid()and P7.is_valid() and P8.is_valid() and P9.is_valid() and P10.is_valid() :
            person = Personal_info.objects.get(id=request.session['person_id'])
        
            P_r1.person = P_r2.person =P_r3.person=P_r4.person=P_r5.person=P_r6.person=P_r7.person=P_r8.person=P_r2.person=P_r9.person=P_r10.person = person
                
            P_r1.pasta_id = P[0].id
            P_r1.rating = P1.cleaned_data.get('rating')
            # print('-----Ratings--',P_r1.rating )
            P_r1.save()
            
            P_r2.pasta_id = P[1].id
            P_r2.rating = P2.cleaned_data.get('rating')
            P_r2.save()       
                    
            P_r3.pasta_id = P[2].id
            P_r3.rating = P3.cleaned_data.get('rating')
            P_r3.save()
            
            
            P_r4.pasta_id = P[3].id
            P_r4.rating = P4.cleaned_data.get('rating')
            P_r4.save()
                    
            P_r5.pasta_id = P[4].id
            P_r5.rating = P5.cleaned_data.get('rating')
            P_r5.save()

            P_r6.pasta_id = P[5].id
            P_r6.rating = P6.cleaned_data.get('rating')
            P_r6.save()
            
            P_r7.pasta_id = P[6].id
            P_r7.rating = P7.cleaned_data.get('rating')
            P_r7.save()
            
            P_r8.pasta_id = P[7].id
            P_r8.rating = P8.cleaned_data.get('rating')
            P_r8.save()
            
            P_r9.pasta_id = P[8].id
            P_r9.rating = P9.cleaned_data.get('rating')
            P_r9.save()
            
            
            P_r10.pasta_id = P[9].id
            P_r10.rating = P10.cleaned_data.get('rating')
            P_r10.save()
            return redirect('image_quality:rate_snacks')
        else: 
            print('not valid')
    else:
       
        P1 = PastaRatingForm(prefix='S1')
        P2 = PastaRatingForm(prefix='S2')
        P3 = PastaRatingForm(prefix='S3')
        P4 = PastaRatingForm(prefix='S4')
        P5 = PastaRatingForm(prefix='S5')
        P6 = PastaRatingForm(prefix='S6')
        P7 = PastaRatingForm(prefix='S7')
        P8 = PastaRatingForm(prefix='S8')
        P9 = PastaRatingForm(prefix='S9')
        P10 = PastaRatingForm(prefix='S10')
    context ={
                        'P1_F': P1,  'P_1':P[0],
                        'P2_F':P2,  'P_2':P[1],
                        'P3_F':P3, 'P_3':P[2],
                        'P4_F':P4, 'P_4':P[3],
                        'P5_F':P5, 'P_5':P[4],
                        
                        'P6_F': P6,  'P_6':P[5],
                        'P7_F':P7,  'P_7':P[6],
                        'P8_F':P8, 'P_8':P[7],
                        'P9_F':P9, 'P_9':P[8],
                        'P10_F':P10, 'P_10':P[9],

    }
  
      
  
    return render(request, 'image_quality/rate_pasta.html', context)

def rate_snacks(request):
    user_selected  = SnacksRating.objects.filter(person_id= request.session['person_id'])
    if user_selected:
        SnacksRating.objects.filter(person_id= request.session['person_id']).delete()
    rated_ones = SnacksRating.objects.all()
    
    
    notRated =  Snacks.objects.exclude(id__in=rated_ones.values('snacks'))
    S = notRated
    
    if request.method == "POST":    
        S1 = SnacksRatingForm(request.POST, prefix='S1')
        
        S2 = SnacksRatingForm(request.POST,prefix='S2')
        S3 = SnacksRatingForm(request.POST,prefix='S3')
        S4 = SnacksRatingForm(request.POST,prefix='S4')
        S5 = SnacksRatingForm(request.POST,prefix='S5')
        S6 = SnacksRatingForm(request.POST,prefix='S6')
        S7 = SnacksRatingForm(request.POST,prefix='S7')
        S8 = SnacksRatingForm(request.POST,prefix='S8')
        S9 = SnacksRatingForm(request.POST,prefix='S9')
        S10 = SnacksRatingForm(request.POST,prefix='S10')
        
        if S1.is_valid():
            print('------------',S1.cleaned_data.get('rating'))
        else:
            print('-----ELSE-------',S1.cleaned_data.get('rating'))
            print('----------', S[0].id)
        
        S_r1 = SnacksRating()
        S_r2 = SnacksRating()
        S_r3 = SnacksRating()
        S_r4 = SnacksRating()
        S_r5 = SnacksRating()
        S_r6 = SnacksRating()
        S_r7 = SnacksRating()
        S_r8 = SnacksRating()
        S_r9 = SnacksRating()
        S_r10 = SnacksRating()
        
        # print('------------',S1.cleaned_data.get('rating'))
        
        if S1.is_valid() and S2.is_valid() and S3.is_valid() and S4.is_valid() and  S5.is_valid() and S6.is_valid() and S7.is_valid() and S8.is_valid() and S9.is_valid() and S10.is_valid() :
            person = Personal_info.objects.get(id=request.session['person_id'])
        
            S_r1.person = S_r2.person =S_r3.person=S_r4.person=S_r5.person=S_r6.person=S_r7.person=S_r8.person=S_r2.person=S_r9.person=S_r10.person = person
                
            S_r1.snacks_id = S[0].id
            S_r1.rating = S1.cleaned_data.get('rating')
            # print('-----Ratings--',S_r1.rating )
            S_r1.save()
            
            S_r2.snacks_id = S[1].id
            S_r2.rating = S2.cleaned_data.get('rating')
            S_r2.save()       
                    
            S_r3.snacks_id = S[2].id
            S_r3.rating = S3.cleaned_data.get('rating')
            S_r3.save()
            
            
            S_r4.snacks_id = S[3].id
            S_r4.rating = S4.cleaned_data.get('rating')
            S_r4.save()
                    
            S_r5.snacks_id = S[4].id
            S_r5.rating = S5.cleaned_data.get('rating')
            S_r5.save()

            S_r6.snacks_id = S[5].id
            S_r6.rating = S6.cleaned_data.get('rating')
            S_r6.save()
            
            S_r7.snacks_id = S[6].id
            S_r7.rating = S7.cleaned_data.get('rating')
            S_r7.save()
            
            S_r8.snacks_id = S[7].id
            S_r8.rating = S8.cleaned_data.get('rating')
            S_r8.save()
            
            S_r9.snacks_id = S[8].id
            S_r9.rating = S9.cleaned_data.get('rating')
            S_r9.save()
            
            
            S_r10.snacks_id = S[9].id
            S_r10.rating = S10.cleaned_data.get('rating')
            S_r10.save()
            return redirect('image_quality:rate_dissert')
        else: 
            print('not valid')
    else:
       
        S1 = SnacksRatingForm(prefix='S1')
        S2 = SnacksRatingForm(prefix='S2')
        S3 = SnacksRatingForm(prefix='S3')
        S4 = SnacksRatingForm(prefix='S4')
        S5 = SnacksRatingForm(prefix='S5')
        S6 = SnacksRatingForm(prefix='S6')
        S7 = SnacksRatingForm(prefix='S7')
        S8 = SnacksRatingForm(prefix='S8')
        S9 = SnacksRatingForm(prefix='S9')
        S10 = SnacksRatingForm(prefix='S10')
    context ={
                        'S1_F': S1,  's_1':S[0],
                        'S2_F':S2,  's_2':S[1],
                        'S3_F':S3, 's_3':S[2],
                        'S4_F':S4, 's_4':S[3],
                        'S5_F':S5, 's_5':S[4],
                        
                        'S6_F': S6,  's_6':S[5],
                        'S7_F':S7,  's_7':S[6],
                        'S8_F':S8, 's_8':S[7],
                        'S9_F':S9, 's_9':S[8],
                        'S10_F':S10, 's_10':S[9],

    }
  
      
  
    return render(request, 'image_quality/rate_snacks.html', context)

def rate_dissert(request):
    user_selected  = DissertRating.objects.filter(person_id= request.session['person_id'])
    if user_selected:
        DissertRating.objects.filter(person_id= request.session['person_id']).delete()
    
    
    rated_ones = DissertRating.objects.all()
    
    
    notRated =  Dissert.objects.exclude(id__in=rated_ones.values('dissert'))
    S = notRated
    
    if request.method == "POST":    
        S1 = DissertRatingForm(request.POST, prefix='S1')
        
        S2 = DissertRatingForm(request.POST,prefix='S2')
        S3 = DissertRatingForm(request.POST,prefix='S3')
        S4 = DissertRatingForm(request.POST,prefix='S4')
        S5 = DissertRatingForm(request.POST,prefix='S5')
        S6 = DissertRatingForm(request.POST,prefix='S6')
        S7 = DissertRatingForm(request.POST,prefix='S7')
        S8 = DissertRatingForm(request.POST,prefix='S8')
        S9 = DissertRatingForm(request.POST,prefix='S9')
        S10 = DissertRatingForm(request.POST,prefix='S10')
        
        if S1.is_valid():
            print('------------',S1.cleaned_data.get('rating'))
        else:
            print('-----ELSE-------',S1.cleaned_data.get('rating'))
            print('----------', S[0].id)
        
        S_r1 = DissertRating()
        S_r2 = DissertRating()
        S_r3 = DissertRating()
        S_r4 = DissertRating()
        S_r5 = DissertRating()
        S_r6 = DissertRating()
        S_r7 = DissertRating()
        S_r8 = DissertRating()
        S_r9 = DissertRating()
        S_r10 = DissertRating()
        
        # print('------------',S1.cleaned_data.get('rating'))
        
        if S1.is_valid() and S2.is_valid() and S3.is_valid() and S4.is_valid() and  S5.is_valid() and S6.is_valid() and S7.is_valid() and S8.is_valid() and S9.is_valid() and S10.is_valid() :
            person = Personal_info.objects.get(id=request.session['person_id'])
        
            S_r1.person = S_r2.person =S_r3.person=S_r4.person=S_r5.person=S_r6.person=S_r7.person=S_r8.person=S_r2.person=S_r9.person=S_r10.person = person
                
            S_r1.dissert_id = S[0].id
            S_r1.rating = S1.cleaned_data.get('rating')
            # print('-----Ratings--',S_r1.rating )
            S_r1.save()
            
            S_r2.dissert_id = S[1].id
            S_r2.rating = S2.cleaned_data.get('rating')
            S_r2.save()       
                    
            S_r3.dissert_id = S[2].id
            S_r3.rating = S3.cleaned_data.get('rating')
            S_r3.save()
            
            
            S_r4.dissert_id = S[3].id
            S_r4.rating = S4.cleaned_data.get('rating')
            S_r4.save()
                    
            S_r5.dissert_id = S[4].id
            S_r5.rating = S5.cleaned_data.get('rating')
            S_r5.save()

            S_r6.dissert_id = S[5].id
            S_r6.rating = S6.cleaned_data.get('rating')
            S_r6.save()
            
            S_r7.dissert_id = S[6].id
            S_r7.rating = S7.cleaned_data.get('rating')
            S_r7.save()
            
            S_r8.dissert_id = S[7].id
            S_r8.rating = S8.cleaned_data.get('rating')
            S_r8.save()
            
            S_r9.dissert_id = S[8].id
            S_r9.rating = S9.cleaned_data.get('rating')
            S_r9.save()
            
            
            S_r10.dissert_id = S[9].id
            S_r10.rating = S10.cleaned_data.get('rating')
            S_r10.save()
            return redirect('image_quality:thank_u')
        else: 
            print('not valid')
    else:
       
        S1 = DissertRatingForm(prefix='S1')
        S2 = DissertRatingForm(prefix='S2')
        S3 = DissertRatingForm(prefix='S3')
        S4 = DissertRatingForm(prefix='S4')
        S5 = DissertRatingForm(prefix='S5')
        S6 = DissertRatingForm(prefix='S6')
        S7 = DissertRatingForm(prefix='S7')
        S8 = DissertRatingForm(prefix='S8')
        S9 = DissertRatingForm(prefix='S9')
        S10 = DissertRatingForm(prefix='S10')
    context ={
                        'S1_F': S1,  's_1':S[0],
                        'S2_F':S2,  's_2':S[1],
                        'S3_F':S3, 's_3':S[2],
                        'S4_F':S4, 's_4':S[3],
                        'S5_F':S5, 's_5':S[4],
                        
                        'S6_F': S6,  's_6':S[5],
                        'S7_F':S7,  's_7':S[6],
                        'S8_F':S8, 's_8':S[7],
                        'S9_F':S9, 's_9':S[8],
                        'S10_F':S10, 's_10':S[9],

    }
  
      
  
    return render(request, 'image_quality/rate_dissert.html', context)





def rate_recipes(request):
    print( request.session['n'])
    
    user_selected  = recipesRating.objects.filter(person_id= request.session['person_id'])
    
    
   
    if request.method == "POST":    
        S1 = recipesRatingForm(request.POST, prefix='S1')
        S2 = recipesRatingForm(request.POST,prefix='S2')
        S3 = recipesRatingForm(request.POST,prefix='S3')
        S4 = recipesRatingForm(request.POST,prefix='S4')
        S5 = recipesRatingForm(request.POST,prefix='S5')
        S6 = recipesRatingForm(request.POST,prefix='S6')

        
        
        S_r1 = recipesRating()
        S_r2 = recipesRating()
        S_r3 = recipesRating()
        S_r4 = recipesRating()
        S_r5 = recipesRating()
        S_r6 = recipesRating()

        
        if S1.is_valid() and S2.is_valid() and S3.is_valid() and S4.is_valid() and  S5.is_valid() and S6.is_valid(): 
            person = Personal_info.objects.get(id=request.session['person_id'])
            # person  = recipesRating.objects.filter(person_id= request.session['person_id']).values_list('person_id')
        
            S_r1.person = S_r2.person =S_r3.person=S_r4.person=S_r5.person= S_r6.person=person
            
            S = cache.get('S')
            print(S)
            # S = request.session['rated']
            # print('S',S)
                
            S_r1.recipes_id = S[0].id
            S_r1.rating = S1.cleaned_data.get('rating')
            S_r1.judging = S1.cleaned_data.get('judging')
            S_r1.save()
            
            S_r2.recipes_id = S[1].id
            S_r2.rating = S2.cleaned_data.get('rating')
            S_r2.judging = S2.cleaned_data.get('judging')
            S_r2.save()       
                    
            S_r3.recipes_id = S[2].id
            S_r3.rating = S3.cleaned_data.get('rating')
            S_r3.judging = S3.cleaned_data.get('judging')    
            S_r3.save()
            
            
            S_r4.recipes_id = S[3].id
            S_r4.rating = S4.cleaned_data.get('rating')
            S_r4.judging = S4.cleaned_data.get('judging')
            S_r4.save()
                    
            S_r5.recipes_id = S[4].id
            S_r5.rating = S5.cleaned_data.get('rating')
            S_r5.judging = S5.cleaned_data.get('judging')
            S_r5.save()

            S_r6.recipes_id = S[5].id
            S_r6.rating = S6.cleaned_data.get('rating')
            S_r6.judging = S6.cleaned_data.get('judging')
            S_r6.save()
            
            # print('#######-N-####',request.session['n'])
            if request.session['n'] == 5:
                return redirect('image_quality:thank_u')
            else :
                request.session['n'] += 1
                return redirect('image_quality:rate_recipes')
        else: 
            print('--------->>not valid')
            
    else:
        user_selected  = recipesRating.objects.filter(person_id= request.session['person_id']).values_list('person_id')
        # print('-------------->>',user_selected[0][0], request.session['person_id'])
        
        if user_selected:
            print('------', user_selected[0][0], request.session['person_id'])
            #person_id = request.session['person_id']
            unique_rate = recipesRating.objects.filter(person_id = request.session['person_id'])
            # print('------ uniiiique :',unique_rate,len(unique_rate))
            notRated =  recipes.objects.exclude(id__in=unique_rate.values('recipes')).order_by('?')
            # print('---------',notRated)
            S = notRated
            cache.set('S',S)
            
        else:
            S =  recipes.objects.all().order_by('?')
            print('All--->',S)
            cache.set('S',S)
            # request.session['recipes'] = list(S)

        S1 = recipesRatingForm(prefix='S1')
        S2 = recipesRatingForm(prefix='S2')
        S3 = recipesRatingForm(prefix='S3')
        S4 = recipesRatingForm(prefix='S4')
        S5 = recipesRatingForm(prefix='S5')
        S6 = recipesRatingForm(prefix='S6')

        context ={
                        'S1_F': S1,  's_1':S[0],
                        'S2_F':S2,  's_2':S[1],
                        'S3_F':S3, 's_3':S[2],
                        'S4_F':S4, 's_4':S[3],
                        'S5_F':S5, 's_5':S[4],
                        'S6_F': S6,  's_6':S[5],
                }

        return render(request, 'image_quality/rate_recipes.html', context)
    




def thank_u(request):
    return render(request, 'image_quality/thanks.html', context={'session_id':request.session['session_id']})