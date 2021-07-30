# Generated by Django 3.2.5 on 2021-07-28 15:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubers',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('nicon', 'nicon'), ('sony', 'sony'), ('red', 'red'), ('fugy', 'fugy'), ('panasonic', 'panasonic'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtubers',
            name='category',
            field=models.CharField(choices=[('code', 'code'), ('mobile_review', 'mobile_review'), ('vlogs', 'vlogs'), ('comedy', 'comedy'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('cooking', 'cooking')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtubers',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtubers',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
