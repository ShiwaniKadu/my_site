# Generated by Django 4.2 on 2024-06-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(max_length=200),
        ),
    ]