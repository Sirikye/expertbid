# Generated by Django 3.2.4 on 2021-06-25 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_proposal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='comment',
            new_name='body',
        ),
    ]
