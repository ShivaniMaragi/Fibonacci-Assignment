# Generated by Django 2.2.5 on 2019-09-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fibinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inp_digit', models.CharField(max_length=10)),
                ('out_result', models.CharField(max_length=225)),
                ('time_taken', models.CharField(default=0.0, max_length=225)),
            ],
        ),
    ]
