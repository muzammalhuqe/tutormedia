# Generated by Django 4.2.7 on 2024-02-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0005_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(blank=True, choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10, null=True),
        ),
    ]
