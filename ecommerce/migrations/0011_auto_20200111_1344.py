# Generated by Django 2.2.8 on 2020-01-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_auto_20200105_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Sneakers'), ('A', 'Accesories'), ('OW', 'Outwear')], max_length=2),
        ),
    ]
