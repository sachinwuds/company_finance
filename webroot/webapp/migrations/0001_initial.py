# Generated by Django 3.2.5 on 2021-07-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('company_type', models.IntegerField(blank=True, null=True)),
                ('earnings', models.IntegerField(blank=True, null=True)),
                ('lifetime', models.CharField(blank=True, max_length=25, null=True)),
                ('status', models.CharField(blank=True, max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]