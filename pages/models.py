from django.db import models

# tutorial/models.py
class QuinnEmployee(models.Model):
    employee_ba_id = models.PositiveIntegerField(null=True, blank=True)
    employee_id = models.PositiveIntegerField(blank=False, null=False)
    formatted_name = models.CharField(max_length=150, null=True, blank=True)
    original_start_date = models.DateField(null=True, blank=True)
    employee_class = models.PositiveSmallIntegerField(null=True, blank=True)
    employee_type = models.CharField(max_length=50, null=True, blank=True)
    employee_class_description = models.CharField(max_length=200, null=True, blank=True)
    active_flag = models.BooleanField(null=True, blank=True)
    personnel_area_description = models.CharField(max_length=200, null=True, blank=True)
    personnel_sub_area_description = models.CharField(max_length=150, null=True, blank=True)
    employee_group_description = models.CharField(max_length=150, null=True, blank=True)
    employee_sub_group_description = models.CharField(max_length=150, null=True, blank=True)
    facility_description = models.CharField(max_length=200, null=True, blank=True)
    cost_centre_description = models.CharField(max_length=200, null=True, blank=True)
    employee_level = models.PositiveSmallIntegerField(null=True, blank=True)
    employee_sub_level = models.CharField(max_length=10, null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    job_family = models.CharField(max_length=200, null=True, blank=True)
    purchase_order = models.PositiveIntegerField(null=True, blank=True)
    item_number = models.PositiveIntegerField(null=True, blank=True)
    activity = models.CharField(max_length=150, null=True, blank=True)
    maintenance = models.CharField(max_length=200, null=True, blank=True)
    rrsp = models.CharField(max_length=200, null=True, blank=True)
    loa = models.PositiveSmallIntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=150, null=True, blank=True)


class DelayCode(models.Model):
    delay_code =  models.CharField(max_length=10)
    function_code = models.PositiveIntegerField()
    description = models.CharField(max_length=200)
