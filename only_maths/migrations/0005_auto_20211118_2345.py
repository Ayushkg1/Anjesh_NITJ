# Generated by Django 3.2.6 on 2021-11-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('only_maths', '0004_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='link_specifier_1',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='material',
            name='link_specifier_2',
            field=models.CharField(default='', max_length=50),
        ),
    ]
