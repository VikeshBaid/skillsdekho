# Generated by Django 2.1.7 on 2019-06-21 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillset', '0002_auto_20190621_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city1',
            name='city',
        ),
        migrations.RemoveField(
            model_name='city1',
            name='state',
        ),
        migrations.RemoveField(
            model_name='state',
            name='state',
        ),
        migrations.RemoveField(
            model_name='employeeprofileinfo',
            name='state',
        ),
        migrations.DeleteModel(
            name='City1',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
