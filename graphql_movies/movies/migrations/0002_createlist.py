# Generated by Django 2.2.3 on 2019-10-26 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=100)),
                ('movie_list', models.CharField(max_length=500)),
            ],
        ),
    ]