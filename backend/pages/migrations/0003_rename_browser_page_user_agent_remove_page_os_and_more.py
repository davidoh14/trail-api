# Generated by Django 4.1.7 on 2023-03-09 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_anonymousid_page_anonymous_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='browser',
            new_name='user_agent',
        ),
        migrations.RemoveField(
            model_name='page',
            name='os',
        ),
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='referrer',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
