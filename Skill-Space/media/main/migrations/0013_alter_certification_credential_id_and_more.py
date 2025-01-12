# Generated by Django 4.2.6 on 2024-01-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_achivements_as_post_certification_as_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='credential_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='credential_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
