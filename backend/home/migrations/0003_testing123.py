# Generated by Django 2.2.28 on 2023-04-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_test12'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing123',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testing1234', models.BigIntegerField()),
            ],
        ),
    ]
