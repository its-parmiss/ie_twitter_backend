# Generated by Django 3.1.5 on 2021-01-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0012_image_dir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='account',
            name='profile_image_url',
            field=models.CharField(default='', max_length=280),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
