# Generated by Django 2.2.4 on 2019-08-26 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('clinicuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rg', models.CharField(max_length=7, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('roles.clinicuser',),
        ),
        migrations.DeleteModel(
            name='ClinicUserManager',
        ),
    ]
