# Generated by Django 5.1.6 on 2025-02-20 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('daily_report_no', models.CharField(default='000', max_length=50)),
                ('page', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='ReportData.report')),
            ],
        ),
    ]
