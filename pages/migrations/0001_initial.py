# Generated by Django 4.1.1 on 2022-09-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuinnEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ba_id', models.PositiveIntegerField()),
                ('employee_id', models.PositiveIntegerField()),
                ('formatted_name', models.CharField(max_length=150)),
                ('original_start_date', models.DateTimeField()),
                ('employee_class', models.PositiveSmallIntegerField()),
                ('employee_type', models.CharField(max_length=50)),
                ('employee_class_description', models.CharField(max_length=200)),
                ('active_flag', models.BooleanField()),
                ('personnel_area_description', models.CharField(max_length=200)),
                ('personnel_sub_area_description', models.CharField(max_length=150)),
                ('employee_group_description', models.CharField(max_length=150)),
                ('employee_sub_group_description', models.CharField(max_length=150)),
                ('facility_description', models.CharField(max_length=200)),
                ('cost_centre_description', models.CharField(max_length=200)),
                ('employee_level', models.PositiveSmallIntegerField()),
                ('employee_sub_level', models.CharField(max_length=10)),
                ('termination_date', models.DateTimeField()),
                ('job_family', models.CharField(max_length=200)),
                ('purchase_order', models.PositiveIntegerField()),
                ('item_number', models.PositiveIntegerField()),
                ('activity', models.CharField(max_length=150)),
                ('maintenance', models.CharField(max_length=200)),
                ('rrsp', models.CharField(max_length=200)),
                ('loa', models.PositiveSmallIntegerField()),
                ('nickname', models.CharField(max_length=150)),
            ],
        ),
    ]