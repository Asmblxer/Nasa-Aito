# Generated by Django 5.1.1 on 2024-10-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_blogs_options_alter_creatures_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='creaturecategories',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='creatures',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
    ]
