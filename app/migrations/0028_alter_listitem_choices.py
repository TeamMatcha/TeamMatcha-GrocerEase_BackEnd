# Generated by Django 4.0.1 on 2022-01-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_listitem_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='choices',
            field=models.CharField(blank=True, choices=[('1', 'Produce'), ('2', 'Dairy'), ('3', 'Baked Goods'), ('4', 'Meat and Fish'), ('5', 'Snacks'), ('6', 'Alcohol'), ('7', 'Baby Care'), ('8', 'Canned Goods'), ('9', 'Dry Goods'), ('10', 'Sauces and  Condiments'), ('11', 'Herbs and Spices'), ('12', 'Non-Alcoholic Beverages'), ('13', 'Household and Cleaning'), ('14', 'Health and Beauty'), ('15', 'Pet Care')], max_length=2, null=True),
        ),
    ]
