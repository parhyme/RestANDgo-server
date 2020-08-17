# Generated by Django 3.1 on 2020-08-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileInfo',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=200, null=True)),
                ('battery_level', models.IntegerField(null=True)),
                ('android_version', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
