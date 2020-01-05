# Generated by Django 2.2.8 on 2020-01-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20200105_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Sneakers'), ('A', 'Accesories'), ('OW', 'Outwear')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('D', 'danger'), ('P', 'primary')], max_length=1),
        ),
    ]