# Generated by Django 5.0.3 on 2024-03-20 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0006_alter_aboutitems_image_alter_servicesitem_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutitems',
            old_name='image',
            new_name='allimage',
        ),
        migrations.RenameField(
            model_name='servicesitem',
            old_name='image',
            new_name='allimage',
        ),
    ]
