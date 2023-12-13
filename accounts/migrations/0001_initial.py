# Generated by Django 4.2.6 on 2023-11-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('confrimation_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('married', 'Married'), ('single', 'Single'), ('windowed', 'Windowed'), ('divorced', 'Divorced'), ('others', 'Others')], default='single', max_length=10, null=True)),
                ('cell_group', models.CharField(blank=True, choices=[('bethlehem', 'Bethlehem'), ('judea', 'Judea'), ('jerusalem', 'Jerusalem')], max_length=9, null=True)),
                ('communicant', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=4, null=True)),
                ('service_attend', models.CharField(blank=True, choices=[('kikuyu', 'Kikuyu'), ('english', 'English')], default='kikuyu', max_length=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('married', 'Married'), ('single', 'Single'), ('windowed', 'Windowed'), ('divorced', 'Divorced'), ('others', 'Others')], default='single', max_length=10, null=True)),
                ('communicant', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=4, null=True)),
                ('service_attend', models.CharField(blank=True, choices=[('kikuyu', 'Kikuyu'), ('english', 'English')], default='kikuyu', max_length=7, null=True)),
                ('cell_group', models.CharField(blank=True, choices=[('bethlehem', 'Bethlehem'), ('judea', 'Judea'), ('jerusalem', 'Jerusalem')], default='judea', max_length=9, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('spouse', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.spouse')),
            ],
        ),
    ]
