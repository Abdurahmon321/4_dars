# Generated by Django 5.0.2 on 2024-04-30 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fath', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='fath.category'),
        ),
    ]
