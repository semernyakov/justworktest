# Generated by Django 2.1.7 on 2019-04-01 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basetype', '0007_pagebasetype_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobasetype',
            name='bitrate',
            field=models.PositiveIntegerField(help_text='kbit/s'),
        ),
        migrations.AlterField(
            model_name='audiobasetype',
            name='order',
            field=models.PositiveIntegerField(default=10, help_text='Max value up to 100', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='pagebasetype',
            name='order',
            field=models.PositiveIntegerField(default=10, help_text='Max value up to 100', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='pagebasetype',
            name='slug',
            field=models.SlugField(null=True, unique='True'),
        ),
        migrations.AlterField(
            model_name='textbasetype',
            name='order',
            field=models.PositiveIntegerField(default=10, help_text='Max value up to 100', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='videobasetype',
            name='order',
            field=models.PositiveIntegerField(default=10, help_text='Max value up to 100', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]