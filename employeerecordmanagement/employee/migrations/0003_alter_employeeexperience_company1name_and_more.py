# Generated by Django 5.0 on 2024-01-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employeeeducation_employeeexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeexperience',
            name='company1name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeeexperience',
            name='company2name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeeexperience',
            name='company3name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]