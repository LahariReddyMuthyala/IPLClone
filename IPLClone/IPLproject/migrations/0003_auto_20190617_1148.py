# Generated by Django 2.2.1 on 2019-06-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPLproject', '0002_auto_20190617_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
