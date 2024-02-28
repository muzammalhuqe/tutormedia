# Generated by Django 4.2.7 on 2024-01-17 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TutionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50)),
                ('subject_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tuition_app/media/uploads/')),
                ('tuition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tuitions.tution')),
            ],
        ),
        migrations.CreateModel(
            name='TuitionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tuition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tuitions.tutiondetails')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tuitions.tutiondetails')),
            ],
        ),
    ]