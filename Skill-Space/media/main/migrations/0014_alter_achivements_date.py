# Generated by Django 4.2.6 on 2024-01-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_certification_credential_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achivements',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]