# Generated by Django 3.0.2 on 2021-01-02 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('Nursery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('nursery', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(default='', max_length=100)),
                ('mobile_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Plant Name')),
                ('Price', models.IntegerField()),
                ('nursery', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Nursery.Nursery')),
            ],
        ),
    ]
