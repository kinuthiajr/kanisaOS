# Generated by Django 5.0.3 on 2024-03-14 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Windowed', 'Windowed'), ('Divorced', 'Divorced'), ('Others', 'Others')], default='Single', max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('service_attends', models.CharField(blank=True, choices=[('English', 'English'), ('Kikuyu', 'Kikuyu')], default='Kikuyu', max_length=8, null=True)),
                ('communicant', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=4, null=True)),
                ('cell_group', models.CharField(blank=True, choices=[('Judea', 'Judea'), ('Jerusalem', 'Jerusalem'), ('Bethlehem', 'Bethlehem')], default='Jerusalem', max_length=10, null=True)),
                ('department', models.CharField(blank=True, choices=[('Kama', 'Kama'), ('MoU', 'MoU'), ('Kayo', 'Kayo'), ('Choir', 'Choir')], default='Kama', max_length=6, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Windowed', 'Windowed'), ('Divorced', 'Divorced'), ('Others', 'Others')], max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('service_attends', models.CharField(blank=True, choices=[('English', 'English'), ('Kikuyu', 'Kikuyu')], max_length=8, null=True)),
                ('communicant', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True)),
                ('cell_group', models.CharField(blank=True, choices=[('Judea', 'Judea'), ('Jerusalem', 'Jerusalem'), ('Bethlehem', 'Bethlehem')], max_length=10, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('department', models.CharField(blank=True, choices=[('SundaySCH', 'SundaySCH'), ('Teens', 'Teens')], max_length=10, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('communicant', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='records.memberprofile')),
            ],
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='spouse',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='records.spouse'),
        ),
    ]