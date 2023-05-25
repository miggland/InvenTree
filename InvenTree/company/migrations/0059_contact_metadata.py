# Generated by Django 3.2.19 on 2023-05-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0058_auto_20230515_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='metadata',
            field=models.JSONField(blank=True, help_text='JSON metadata field, for use by external plugins', null=True, verbose_name='Plugin Metadata'),
        ),
    ]
