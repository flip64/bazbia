# Generated by Django 4.2.6 on 2023-11-26 11:55

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('customer', '0005_member_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', django_jalali.db.models.jDateTimeField(auto_now=True)),
                ('sum', models.BigIntegerField()),
                ('pardakht', models.BigIntegerField()),
                ('takhfif', models.IntegerField()),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.member')),
            ],
        ),
        migrations.CreateModel(
            name='ListState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='ListPrudoct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faktor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.faktor')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.product')),
            ],
        ),
        migrations.AddField(
            model_name='faktor',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.liststate'),
        ),
    ]
