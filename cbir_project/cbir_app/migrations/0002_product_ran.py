# Generated by Django 4.2.1 on 2023-06-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbir_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ran',
            field=models.URLField(default='ggg'),
        ),
    ]
