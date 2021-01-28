# Generated by Django 3.1.5 on 2021-01-28 07:06

from django.db import migrations, models
import twitterapp.functions


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0010_auto_20210128_0316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=twitterapp.functions.upload_to)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=twitterapp.functions.upload_to, verbose_name='Image'),
        ),
    ]