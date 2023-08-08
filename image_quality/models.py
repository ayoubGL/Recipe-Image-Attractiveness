from tokenize import Name
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import ChoicesMeta
from django.db.models.fields import AutoField, CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from .choices import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

# Create your models here.


class Personal_info(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='Personal_info')

    created = models.DateTimeField(auto_now_add=True)

    age = models.CharField(max_length=120,
                           choices=Age_choices,
                           verbose_name='age',
                           default=None,
                           blank=False
                           )

    country = CountryField(blank_label='')

    education = models.CharField(max_length=120,
                                 choices=EducationLevel,
                                 verbose_name='education',
                                 default=None,
                                 blank=False

                                 )


    gender = models.CharField(max_length=300,
                              choices=Gender_choices,
                              verbose_name='gender',
                              default=None,
                              blank=False
                              )
    FK_9 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_9',
                             default=None,
                             blank = False)
    FK_10 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_10',
                             default=None,
                             blank = False)
    FK_11 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_11',
                             default=None,
                             blank = False)
    FK_12 = models.CharField(max_length = 300,
 			    choices = FK__choices,
			  verbose_name = 'FK_12',
			default = None,
			blank = False)




    # other_diet = models.CharField(("other_diet"), max_length=50, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'personal_info'
        ordering = ['id']
        db_table = 'personal_info'

    def __str__(self):
        return "{}".format(self.id)
    
    
    
class Salad(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField( max_length=500)
    image_link = models.CharField( max_length=500)
    # rating = models.CharField( max_length=500)
    
    class Meta:
        verbose_name = "salad"
        ordering  = ['id']
        db_table = 'Salad'
    def __str__(self):
        return self.Name
    

class SaladRating(models.Model):
    id = models.AutoField(primary_key=True)
    # Name = models.CharField( max_length=500)
    image_link = models.CharField( max_length=500)
    rating = models.CharField( max_length=500,
                              choices = ratings,
                              verbose_name = 'ratings',
                              default=None,
                              blank = False
                              
                              )
    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )
    salad = models.ForeignKey(
        Salad,
        on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = "saladrating"
        ordering  = ['id']
        db_table = 'Saladrating'
    def __str__(self):
        return self.salad.Name