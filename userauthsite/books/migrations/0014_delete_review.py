# Generated by Django 5.0.4 on 2024-05-09 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_book_release_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
