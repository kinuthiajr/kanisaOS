# Generated by Django 4.2.6 on 2024-01-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_children_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='dept',
            field=models.CharField(blank=True, choices=[('sunday_sch', 'Sunday_Sch'), ('teens', 'Teens')], max_length=11, null=True),
        ),
    ]