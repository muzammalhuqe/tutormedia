# Generated by Django 4.2.7 on 2024-02-28 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0020_alter_comment_tution_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tution_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tuitions.tutiondetails'),
        ),
    ]