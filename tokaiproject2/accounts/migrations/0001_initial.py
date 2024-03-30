# Generated by Django 5.0.1 on 2024-01-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(default='default_text_value')),
                ('thumbnail', models.ImageField(default='default_thumbnail.jpg', upload_to='')),
            ],
        ),
    ]