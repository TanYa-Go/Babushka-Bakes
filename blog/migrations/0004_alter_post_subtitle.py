# Generated by Django 3.2.8 on 2021-11-23 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=254),
        ),
    ]
