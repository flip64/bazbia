# Generated by Django 4.2.6 on 2023-12-10 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0034_alter_aqhsat_aghsat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aqhsat',
            name='aghsat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.dafteraqhsat'),
        ),
    ]
