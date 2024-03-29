# Generated by Django 4.2.7 on 2024-01-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0004_tutiondetails_tuition_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone_no', models.CharField(max_length=13)),
                ('comments', models.TextField()),
            ],
        ),
    ]
