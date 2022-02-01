# Generated by Django 4.0.1 on 2022-01-26 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_listitem_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='app.category'),
        ),
    ]