# Generated by Django 3.2.6 on 2022-09-18 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_created=True)),
                ('email', models.EmailField(default='email', max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='cities',
            name='created',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cities',
            name='state',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='created',
        ),
        migrations.RemoveField(
            model_name='country',
            name='created',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='sortname',
        ),
        migrations.RemoveField(
            model_name='states',
            name='country',
        ),
        migrations.RemoveField(
            model_name='states',
            name='created',
        ),
        migrations.RemoveField(
            model_name='states',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testimonails',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user_gallery',
            name='created',
        ),
        migrations.RemoveField(
            model_name='website_gallery',
            name='created',
        ),
        migrations.AddField(
            model_name='user_detail',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_detail',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.subcategory'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='cities',
            table=None,
        ),
        migrations.AlterModelTable(
            name='country',
            table=None,
        ),
        migrations.AlterModelTable(
            name='states',
            table=None,
        ),
    ]