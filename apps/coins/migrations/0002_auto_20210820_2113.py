# Generated by Django 3.2.6 on 2021-08-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='advantages',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='coin',
            name='disadvantages',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='coin',
            name='working',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
