# Generated by Django 3.0.7 on 2021-02-04 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_auto_20210204_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testreport',
            name='name',
            field=models.CharField(help_text='Template name', max_length=100, verbose_name='Name'),
        ),
    ]