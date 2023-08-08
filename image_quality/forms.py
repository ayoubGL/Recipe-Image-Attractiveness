
from django import forms
from django.core.exceptions import ValidationError
from django.db import close_old_connections, models
from django.db.models import fields
from django.forms import widgets
from .models import Personal_info, Salad, SaladRating
from django_starfield import Stars
from django.forms import formset_factory, modelformset_factory


class Personal_infoForm(forms.ModelForm):
    class Meta:
        model = Personal_info
        exclude = ('id', 'created', 'title', 'session_id')
        widgets = {
            'gender': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'age': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            'country': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'education': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            
            'FK_9'  : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_10' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_11' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True}),
            'FK_12' : forms.Select(attrs={'class':'form-select form-select-sm clabel','required':True})
        }
        labels = {
            'gender': 'Gender',
            'age': 'Age',
            'country': 'Country of residence',
            'education': 'Your highest completed education',

        # food knowledge
            'FK_9' : 'Compared with an average person, I know a lot about healthy eating',
            'FK_10': 'I think I know enough about healthy eating to feel pretty confident when choosing a recipe',
            'FK_11': 'I know a lot about how to evaluate the healthiness of a recipe',
            'FK_12': 'I do NOT feel very knowledgeable about healthy eating'

        }


class SaladRatingForm(forms.ModelForm):
    # ratings = forms.IntegerField(required= True, widget=Stars(), error_messages={'required':'Please rate this recipe'}, label='')
    class Meta:
        model=SaladRating
        exclude=('id', 'person')
        widgets = {
            'rating':forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True, 'label_suffix':'', }, ) 
        }
        labels = {
            'rating':'',
            'image_link':'',
            'salad':''
        }