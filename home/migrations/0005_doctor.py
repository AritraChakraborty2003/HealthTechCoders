# Generated by Django 4.2.5 on 2023-10-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_patid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.TextField()),
                ('experience', models.TextField()),
                ('Degree', models.TextField()),
                ('Specialist', models.TextField()),
            ],
        ),
    ]
