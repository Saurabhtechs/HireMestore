from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_img', models.ImageField(max_length=250, upload_to='img')),
                ('description', models.TextField()),
                ('member_name', models.CharField(max_length=50)),
                ('member_img', models.ImageField(max_length=250, upload_to='img')),
                ('member_skill', models.CharField(max_length=30)),
                ('fb_link', models.CharField(max_length=75)),
                ('twitter_link', models.CharField(max_length=75)),
                ('insta_link', models.CharField(max_length=75)),
                ('email_link', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=250, upload_to='img')),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('type', models.IntegerField(default=1)),
                ('feature', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=75)),
                ('mobile', models.IntegerField(unique=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(max_length=250, upload_to='img')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('about', models.CharField(max_length=50)),
                ('review', models.CharField(max_length=200)),
            ],
        ),
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
                ('trusted_by', models.FileField(upload_to='img')),
                ('fb_link', models.CharField(max_length=250)),
                ('twitter_link', models.CharField(max_length=250)),
                ('instagram_link', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('sub_category', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('experiance', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('discription', models.TextField()),
                ('message', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=250, upload_to='img')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('feature', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
