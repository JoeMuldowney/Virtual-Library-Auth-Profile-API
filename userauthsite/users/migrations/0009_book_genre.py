# Generated by Django 5.0.4 on 2024-04-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_book_book_description_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
