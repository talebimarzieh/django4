# Generated by Django 4.2.4 on 2023-08-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_dtm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='dtm',
            field=models.CharField(default=100.14285714285714, max_length=10),
        ),
    ]
