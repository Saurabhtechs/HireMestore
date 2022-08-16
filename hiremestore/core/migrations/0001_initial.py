# Generated by Django 3.2.6 on 2022-08-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='website_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(max_length=250, upload_to='img')),
                ('mobile_number', models.CharField(max_length=15)),
                ('website_title', models.CharField(max_length=50)),
                ('website_subtitle', models.CharField(max_length=100)),
                ('background_img', models.ImageField(max_length=250, upload_to='img')),
                ('favicon', models.ImageField(max_length=250, upload_to='img')),
                ('trusted_by', models.ImageField(max_length=250, upload_to='img')),
                ('fb_link', models.CharField(max_length=250)),
                ('twitter_link', models.CharField(max_length=250)),
                ('instagram_link', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
