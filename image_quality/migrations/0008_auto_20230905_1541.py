# Generated by Django 3.2.6 on 2023-09-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_quality', '0007_auto_20230905_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ghs_fk',
            old_name='FK_2',
            new_name='FK_10',
        ),
        migrations.RenameField(
            model_name='ghs_fk',
            old_name='FK_4',
            new_name='FK_12',
        ),
        migrations.RenameField(
            model_name='ghs_fk',
            old_name='FK_1',
            new_name='FK_9',
        ),
        migrations.RemoveField(
            model_name='ghs_fk',
            name='FK_3',
        ),
        migrations.RemoveField(
            model_name='ghs_fk',
            name='FK_5',
        ),
        migrations.RemoveField(
            model_name='ghs_fk',
            name='FK_6',
        ),
        migrations.RemoveField(
            model_name='ghs_fk',
            name='FK_7',
        ),
        migrations.RemoveField(
            model_name='ghs_fk',
            name='FK_8',
        ),
        migrations.AddField(
            model_name='ghs_fk',
            name='FK_11',
            field=models.CharField(choices=[(None, ''), ('Strongly_Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly_Agree', 'Strongly Agree')], default=None, max_length=300, verbose_name='FK_3'),
        ),
    ]
