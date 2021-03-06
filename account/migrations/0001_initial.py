# Generated by Django 2.2.6 on 2020-01-15 10:31

import account.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=13, validators=[account.validators.validate_phone])),
                ('self_description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ManyToManyField(to='account.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Role')),
            ],
            bases=('account.role',),
        ),
        migrations.CreateModel(
            name='CustomRole',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Role')),
                ('name', models.CharField(max_length=80)),
            ],
            bases=('account.role',),
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Role')),
                ('since', models.DateField()),
            ],
            bases=('account.role',),
        ),
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Role')),
                ('name', models.CharField(max_length=80)),
            ],
            bases=('account.role',),
        ),
        migrations.CreateModel(
            name='PastDirector',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Role')),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
            ],
            bases=('account.role',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('role_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Role')),
                ('title', models.CharField(max_length=40)),
            ],
            bases=('account.role',),
        ),
    ]
