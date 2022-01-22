# Generated by Django 4.0.1 on 2022-01-22 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_listitem_item_listitem_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='users',
        ),
        migrations.AddField(
            model_name='list',
            name='user_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
