# Generated by Django 5.0.7 on 2024-07-22 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=70)),
                ('phone_no', models.CharField(default='', max_length=200)),
                ('email', models.BooleanField(default=False)),
                ('address', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Category', models.CharField(default='Family', max_length=100)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
    ]
