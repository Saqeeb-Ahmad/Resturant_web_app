# Generated by Django 5.0.3 on 2024-03-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_ourstory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ourstory_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_from',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutitems',
            name='ourstory',
        ),
    ]