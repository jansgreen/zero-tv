# Generated by Django 3.0.7 on 2020-11-18 17:16

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=50, null=True)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=11)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcade', models.IntegerField()),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address', models.CharField(max_length=80)),
                ('county', models.CharField(max_length=80, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('original_bag', models.TextField(default='')),
                ('stripe_paid', models.CharField(default='', max_length=254)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('lineitem_total', models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=6)),
                ('Movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Movies')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
            ],
        ),
    ]
