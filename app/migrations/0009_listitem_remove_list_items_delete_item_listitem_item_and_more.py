# Generated by Django 4.0.1 on 2022-01-20 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_locations'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='list',
            name='items',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='listitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_item', to='app.list'),
        ),
        migrations.AddField(
            model_name='listitem',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='items', to='app.Product'),
        ),
    ]