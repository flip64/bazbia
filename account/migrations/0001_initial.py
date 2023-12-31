# Generated by Django 4.2.6 on 2023-11-20 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageCate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dis', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Ename', models.CharField(default=None, max_length=100)),
                ('dis', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('order', models.IntegerField(default=1)),
                ('pageENnam', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150)),
                ('dis', models.CharField(blank=True, max_length=200, null=True)),
                ('PageCate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.pagecate')),
            ],
        ),
        migrations.CreateModel(
            name='AccessList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dis', models.CharField(blank=True, max_length=200, null=True)),
                ('page', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='account.page')),
                ('role', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='account.role')),
            ],
            options={
                'ordering': ['role'],
            },
        ),
    ]
