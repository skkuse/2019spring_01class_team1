# Generated by Django 2.1.2 on 2019-06-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20190604_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ball_foot',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='shoes_size',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]