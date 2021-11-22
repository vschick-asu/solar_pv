# Generated by Django 3.2.7 on 2021-11-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('report_number', models.IntegerField()),
                ('issue_date', models.IntegerField()),
                ('standard_id', models.IntegerField()),
                ('location_id', models.IntegerField()),
                ('model_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('is_fi_required', models.CharField(max_length=20)),
                ('standard_id', models.IntegerField()),
            ],
        ),
    ]