# Generated by Django 4.2.6 on 2023-11-14 09:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CateL1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='CateL2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catel1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catel1')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enName', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='upload/collection')),
            ],
        ),
        migrations.CreateModel(
            name='Daste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enghlishNmae', models.CharField(blank=True, max_length=50, null=True)),
                ('picture', models.ImageField(default='upload/dasteh/defult.jpg', upload_to='upload/dasteh')),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='upload/slidepic')),
                ('disSmall', models.TextField()),
                ('disBig', models.TextField()),
                ('state', models.CharField(blank=True, default='', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('price', models.BigIntegerField(default=0)),
                ('takhfif', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('picture', models.ImageField(upload_to='upload/product')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.catel2')),
            ],
        ),
        migrations.CreateModel(
            name='Moshabe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productOne', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='poduct2product', to='shop.product')),
                ('productTWO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='kalayeMoshabeh', to='shop.product')),
            ],
        ),
        migrations.CreateModel(
            name='DasteProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daste', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.daste')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.product')),
            ],
        ),
    ]
