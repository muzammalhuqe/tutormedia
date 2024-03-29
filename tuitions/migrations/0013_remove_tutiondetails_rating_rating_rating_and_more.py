# Generated by Django 4.2.7 on 2024-02-27 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuitions', '0012_remove_comment_rating_comment_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutiondetails',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.CharField(blank=True, choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='tuton',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tuitions.tutiondetails'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
