# Generated by Django 4.0.5 on 2022-07-21 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_application_no_of_persons_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='save_details',
        ),
    ]
