# Generated by Django 4.1.1 on 2022-10-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_quinnemployee_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quinnemployee',
            name='nickname',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='quinnemployee',
            name='original_start_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
