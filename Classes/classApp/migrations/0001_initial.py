# Generated by Django 3.1.3 on 2020-11-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('Course_Number', models.IntegerField()),
                ('Instructor_Name', models.CharField(max_length=60)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]
