
from django import forms
from django.core.exceptions import ValidationError
from django.db import close_old_connections, models
from django.db.models import fields
from django.forms import widgets
from .models import Personal_info, Salad, SaladRating,PastaRating,SnacksRating, DissertRating, recipesRating, Ghs_fk
from django_starfield import Stars
from django.forms import formset_factory, modelformset_factory
from .choices import *


class Personal_infoForm(forms.ModelForm):
    class Meta:
        model = Personal_info
        exclude = ('id', 'created', 'title', 'session_id')
        widgets = {
            'gender': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'age': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            'country': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'education': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            
            # 'FK_9'  : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # 'FK_10' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # 'FK_11' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # 'FK_12' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # 'FK_12' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # # 'FK_13' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # 'FK_14' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            # 'FK_15' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
        }
        labels = {
            'gender': 'Gender',
            'age': 'Age',
            'country': 'Country of residence',
            'education': 'Your highest completed education',

        # # food knowledge
        #     'FK_9' : 'I can confidently cook recipes with basic ingredients',
        #     'FK_10': 'I can confidently follow all the steps of a simple recipes',
        #     'FK_11': 'I can confidently taste new foods',
        #     'FK_12': 'I can confidently cook new foods and try new recipes',
        #     # 'FK_13':'The frequency of cooking main meal from raw or basic ingredients',
        #     'FK_14':'I enjoy cooking',
        #     'FK_15':'Are you satisfied with you cooking skills'
                

        }
class Ghs_fkForm(forms.ModelForm):
    class Meta:
        model = Ghs_fk
        exclude = ('id','person','created','title','session_id')
        widgets = {
            'FK_9'  : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_10' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_11' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_12' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            
            
            'CS_9'  : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CS_10' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CS_11' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CS_12' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CS_13' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CS_14' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'CS_15' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
           
        } 

        labels = {



            'FK_9' : 'Compared with an average person, I know a lot about healthy eating',
            'FK_10': 'I think I know enough about healthy eating to feel pretty confident when choosing a recipe',
            'FK_11': 'I know a lot about how to evaluate the healthiness of a recipe',
            'FK_12': 'I do NOT feel very knowledgeable about healthy eating',
            
            'CS_9' : 'I can confidently cook recipes with basic ingredients',
            'CS_10': 'I can confidently follow all the steps of a simple recipes',
            'CS_11': 'I can confidently taste new foods',
            'CS_12': 'I can confidently cook new foods and try new recipes',
            'CS_13':'I enjoy cooking',
            'CS_14':'Are you satisfied with you cooking skills'
            
            
        }





class SaladRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=ratings, widget=forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', },))
    
    class Meta:
        model=SaladRating
        exclude=('id', 'person','salad')
        widgets = {
            
            'judging': forms.Textarea(attrs={'required': True, 'label_suffix':'', 'class':'btn-lgT', 'placeholder':'here', 'rows':5, 'cols':30,})
            # 'rating':forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'}, ) 
        }
        labels = {
            # 'rating':'',
            'image_link':'',
            'salad':''
        }
        
class PastaRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=ratings, widget=forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg',},))
    class Meta:
        model=PastaRating
        exclude=('id', 'person','pasta')
        widgets = {
            # 'rating':forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'}, ) 
        }
        labels = {
            # 'rating':'',
            'image_link':'',
            'pasta':''
        }
        
        
class SnacksRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=ratings, widget=forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'},))
    class Meta:
        model=SnacksRating
        exclude=('id', 'person','snacks')
        widgets = {
            # 'rating':forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'}, ) 
        }
        labels = {
            # 'rating':'',
            'image_link':'',
            'snacks':''
        }
        
        
        

class DissertRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=ratings, widget=forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'},))
    class Meta:
        model=DissertRating
        exclude=('id', 'person','dissert')
        widgets = {
            # 'rating':forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'}, ) 
        }
        labels = {
            # 'rating':'',
            'image_link':'',
            'dissert':''
        }
        
    
class recipesRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=ratings, widget=forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', },))
    
    class Meta:
        model=recipesRating
        exclude=('id', 'person','recipes')
        widgets = {
            
            'judging': forms.Textarea(attrs={'required': True, 'label_suffix':'', 'class':'btn-lgT', 'placeholder':'Please write one sentence about why you have given this rating', 'rows':5, 'cols':30,})
            # 'rating':forms.Select(attrs={'required': True, 'label_suffix':'', 'class':'btn-lg', 'placeholder':'here'}, ) 
        }
        labels = {
            # 'rating':'',
            'image_link':'',
            'recipes':''
        }