# Generated by Django 4.2.4 on 2023-08-14 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_contact_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='descrition',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='emai',
            new_name='email',
        ),
    ]