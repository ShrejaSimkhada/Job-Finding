# Generated by Django 3.2.12 on 2022-03-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findingJob', '0011_alter_jobdetail_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='salary',
            field=models.FloatField(max_length=200, null=True),
        ),
    ]
