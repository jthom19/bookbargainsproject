# Generated by Django 3.1.7 on 2021-05-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbapp', '0015_book_reported'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ISBN13Conf',
            field=models.CharField(max_length=13, null=True),
        ),
    ]