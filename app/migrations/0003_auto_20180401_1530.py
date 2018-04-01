# Generated by Django 2.0.3 on 2018-04-01 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_content_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='fire_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
