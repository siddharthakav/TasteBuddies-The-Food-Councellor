# Generated by Django 2.2.14 on 2022-11-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0027_auto_20221120_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_Vegan',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
