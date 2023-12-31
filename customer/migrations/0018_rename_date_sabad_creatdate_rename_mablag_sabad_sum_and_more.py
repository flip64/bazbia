# Generated by Django 4.2.6 on 2023-11-27 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_productfaktor_pricejam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sabad',
            old_name='date',
            new_name='creatDate',
        ),
        migrations.RenameField(
            model_name='sabad',
            old_name='mablag',
            new_name='sum',
        ),
        migrations.AddField(
            model_name='sabad',
            name='pardakht',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sabad',
            name='takhfif',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
