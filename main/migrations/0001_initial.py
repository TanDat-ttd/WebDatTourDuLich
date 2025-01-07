# Generated by Django 5.1.4 on 2025-01-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=10, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.PositiveIntegerField()),
                ('remaining_capacity', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='tour_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
