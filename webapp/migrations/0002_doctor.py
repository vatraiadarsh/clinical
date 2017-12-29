# Generated by Django 2.0 on 2017-12-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=128)),
                ('specialty', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=128)),
            ],
        ),
    ]