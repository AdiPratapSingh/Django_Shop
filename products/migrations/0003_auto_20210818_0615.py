# Generated by Django 3.2.6 on 2021-08-18 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Buy_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=2083),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='image_url',
            field=models.CharField(max_length=2083),
        ),
    ]