# Generated by Django 4.2.6 on 2023-11-25 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_spouse_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spouse',
            old_name='confrimation_date',
            new_name='confirmation_date',
        ),
    ]
