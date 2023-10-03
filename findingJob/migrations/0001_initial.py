# Generated by Django 3.2.12 on 2022-03-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Out for delivery')], max_length=200, null=True)),
                ('salary', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('responsibility', models.CharField(max_length=1000, null=True)),
                ('qualification', models.CharField(max_length=1000, null=True)),
                ('published_date', models.DateField(max_length=200, null=True)),
                ('deadline_date', models.DateField(max_length=200, null=True)),
                ('no_of_vaccinies', models.CharField(max_length=200, null=True)),
                ('company_details', models.CharField(max_length=200, null=True)),
                ('company_logo', models.ImageField(blank=True, default='defaultlogo.png', null=True, upload_to='')),
            ],
        ),
    ]