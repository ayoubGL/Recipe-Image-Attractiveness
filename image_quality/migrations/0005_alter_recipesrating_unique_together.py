# Generated by Django 3.2.6 on 2023-08-31 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_quality', '0004_alter_recipesrating_recipes'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipesrating',
            unique_together={('person', 'recipes')},
        ),
    ]
