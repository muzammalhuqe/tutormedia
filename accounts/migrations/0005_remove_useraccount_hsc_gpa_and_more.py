# Generated by Django 4.2.7 on 2024-02-26 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_useraccount_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='hsc_gpa',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='hsc_roll',
        ),
    ]