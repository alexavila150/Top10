# Generated by Django 4.0.3 on 2022-04-10 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.CharField(default='lb', max_length=10),
            preserve_default=False,
        ),
    ]
