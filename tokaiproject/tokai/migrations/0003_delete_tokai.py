# Generated by Django 5.0.1 on 2024-01-29 07:51

from django.db import migrations
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tokai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='user',
            field=models.ForeignKey(to='auth.User', on_delete=models.CASCADE),
        ),
    ]

    