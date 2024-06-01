# Generated by Django 4.2.6 on 2024-01-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_project_profession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profession',
        ),
        migrations.AddField(
            model_name='professional_profile',
            name='profession',
            field=models.CharField(default='Software Engineer', max_length=225),
        ),
    ]