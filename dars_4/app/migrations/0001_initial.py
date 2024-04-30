# Generated by Django 5.0.2 on 2024-04-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('area', models.IntegerField()),
                ('img', models.ImageField(upload_to='card_imgs/')),
                ('population', models.BigIntegerField()),
            ],
        ),
    ]