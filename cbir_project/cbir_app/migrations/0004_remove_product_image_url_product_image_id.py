# Generated by Django 4.2.1 on 2023-06-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbir_app', '0003_remove_product_ran'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image_id',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
