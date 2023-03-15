# Generated by Django 4.1.7 on 2023-03-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_apikey_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='active',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='website',
            name='active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]