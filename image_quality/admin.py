from django.contrib import admin
from django.db.models.base import Model
from .models import *
# Register your models here.
import csv
from django.http import HttpResponse

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportMixin
from django import forms


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


def export_as_csv_action(description="Export selected objects as CSV file", fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = [field.name for field in opts.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


    export_as_csv.short_description = description
    return export_as_csv

# @admin.register(Personal_info)
class Personal_infoAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id','session_id','created','age','gender','country','education','FK_9',
    'FK_10','FK_11','FK_12','FK_13','FK_14', 'FK_15')
    actions = [export_as_csv_action("CSV Export")]

class SaladAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id',
    'Name',
    'image_link',
   ))
    actions = [export_as_csv_action("CSV Export")]
    
    

class PastaAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id',
    'Name',
    'image_link',
   ))
    actions = [export_as_csv_action("CSV Export")]
    

class DissertAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id',
    'Name',
    'image_link',
   ))
    actions = [export_as_csv_action("CSV Export")]    


class SnacksAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id',
    'Name',
    'image_link',
   ))
    actions = [export_as_csv_action("CSV Export")]
    
class SaladRatingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id', 'person',
    'rating','salad','judging'
    # 'image_link',
    ))
    actions = [export_as_csv_action("CSV Export")]
    
class PastaRatingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id', 'person',
    'rating','pasta','judging'
    # 'image_link',
    ))
    actions = [export_as_csv_action("CSV Export")] 
    

class DissertRatingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id', 'person',
    'rating','dissert','judging'
    # 'image_link',
    ))
    actions = [export_as_csv_action("CSV Export")]  
    
class SnacksRatingAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = (('id', 'person',
    'rating','snacks','judging'
    # 'image_link',
    ))
    actions = [export_as_csv_action("CSV Export")]  

admin.site.register(Personal_info, Personal_infoAdmin)

admin.site.register(Salad, SaladAdmin)
admin.site.register(SaladRating, SaladRatingAdmin)

admin.site.register(Pasta, PastaAdmin)
admin.site.register(PastaRating, PastaRatingAdmin)

admin.site.register(Snacks, SnacksAdmin)
admin.site.register(SnacksRating, SnacksRatingAdmin)

admin.site.register(Dissert, DissertAdmin)
admin.site.register(DissertRating, DissertRatingAdmin)

