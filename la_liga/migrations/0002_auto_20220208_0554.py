# Generated by Django 3.2.12 on 2022-02-08 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('la_liga', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='injuered',
            new_name='injured',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='postion',
            new_name='position',
        ),
    ]
