# Generated by Django 3.2.6 on 2022-09-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_user_detail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_detail',
            name='charges',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
