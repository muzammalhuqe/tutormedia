# Generated by Django 4.2.7 on 2024-02-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0017_alter_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[('⭐', 1), ('⭐⭐', 2), ('⭐⭐⭐', 3), ('⭐⭐⭐⭐', 4), ('⭐⭐⭐⭐⭐', 5)], default=1),
        ),
    ]
