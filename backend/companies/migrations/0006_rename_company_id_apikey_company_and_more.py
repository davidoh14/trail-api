# Generated by Django 4.1.7 on 2023-03-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_company_active_website_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikey',
            old_name='company_id',
            new_name='company',
        ),
        migrations.AlterField(
            model_name='company',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]