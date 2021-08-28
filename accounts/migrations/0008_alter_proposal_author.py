# Generated by Django 3.2.4 on 2021-07-07 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_proposal_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
