# Generated by Django 2.0.6 on 2018-06-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_name', models.CharField(max_length=200)),
                ('d_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('d_chair', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'departments',
                'ordering': ['d_name'],
            },
        ),
    ]
