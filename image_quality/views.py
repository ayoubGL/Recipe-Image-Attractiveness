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
from .forms import Personal_infoForm, SaladRatingForm,Salad


# from .forms import Personal_infoForm, FoodCategory, FoodCategoryForm,ChoiceEvaluationForm
# from django.forms import formset_factory, modelformset_factory
from .models import  Personal_info, SaladRating
# from .app import *
# Create your views here.
# person_id = 0
import string
import random
import re
# Create your views here.


def home(request):
    request.session['person_id'] = 0
    #prolific_id = , msg)
    #prolific_id = str(prolific_id.group(1))
    full_url = request.get_full_path()
    #request.GET['PROLIFIC_PID']
    print('Full',request.get_full_path())
    #print(full_url)
    if 'PROLIFIC_PID' in full_url:
        prolific_id = re.search("PROLIFIC_PID=(.*?)&STUDY_ID",full_url)
        request.session['prolific_id'] = str(prolific_id.group(1))
        #print("----------",prolific_id.group(1))
    else:
        request.session['prolific_id'] = '000'
    return render(request, 'image_quality/homes.html')

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

            request.session['person_id'] = answer.id
            return redirect('image_quality:rate_salad')
    else:
        personl_info = Personal_infoForm()
    return render(request, 'image_quality/personal_info.html', context={'form': personl_info})

def rate_salad(request):
    user_selected  = SaladRating.objects.filter(person_id= request.session['person_id'])
    if user_selected:
        SaladRating.objects.filter(person_id= request.session['person_id']).delete()
    S = Salad.objects.all()
    # for i in range(len(S)):
    #     print("-------->",S[i].Name)
    
    
        
    
    if request.method == "POST":    
        S1 = SaladRatingForm(request.POST, prefix='S1')

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
                        'S1': S1, 'S1':rcp[0],
                        'S2':S2, 'S2': rcp[1],
                        'S3':S3, 'S3': rcp[2],
                        'S4':S4, 'S4': rcp[3],
                        'S5':S5, 's5': rcp[4],

    }
  
      
  
    return render(request, 'image_quality/rate_salad.html', context = {'form':S1})
