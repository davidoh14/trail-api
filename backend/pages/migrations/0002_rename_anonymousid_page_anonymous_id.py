# Generated by Django 4.1.7 on 2023-03-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='anonymousID',
            new_name='anonymous_id',
        ),
    ]
