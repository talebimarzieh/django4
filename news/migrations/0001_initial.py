# Generated by Django 4.2.4 on 2023-08-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('txt', models.TextField(max_length=100)),
                ('editor', models.CharField(max_length=15)),
            ],
        ),
    ]