# Generated by Django 4.2.7 on 2024-02-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0010_remove_rating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.ManyToManyField(blank=True, null=True, to='tuitions.rating'),
        ),
    ]