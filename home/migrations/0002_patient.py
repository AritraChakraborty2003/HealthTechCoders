# Generated by Django 4.2.5 on 2023-10-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.TextField()),
                ('sex', models.TextField()),
                ('history', models.TextField()),
            ],
        ),
    ]
