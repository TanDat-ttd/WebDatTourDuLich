# Generated by Django 5.1.4 on 2025-01-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='plain_password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
