# Generated by Django 3.1.7 on 2021-05-12 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbapp', '0025_auto_20210511_0143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['price']},
        ),
        migrations.AddField(
            model_name='profile',
            name='field',
            field=models.CharField(choices=[('SO', 'Select One'), ('ART', 'Arts'), ('MSC', 'Music'), ('HST', 'History'), ('LNG', 'Languages'), ('LAW', 'Law'), ('PHL', 'Philosophy'), ('THE', 'Theology'), ('ECN', 'Economics'), ('PLS', 'Political Science'), ('PSY', 'Psychology'), ('SOC', 'Sociology'), ('NUR', 'Nursing'), ('BIO', 'Biology'), ('CHM', 'Chemistry'), ('PHY', 'Physics'), ('ENG', 'Engineering'), ('CSC', 'Computer Science'), ('MTH', 'Mathematics'), ('BUS', 'Business'), ('FIN', 'Finance'), ('ACT', 'Accounting'), ('OTH', 'Other')], default='Select One', max_length=4, null=True),
        ),
    ]