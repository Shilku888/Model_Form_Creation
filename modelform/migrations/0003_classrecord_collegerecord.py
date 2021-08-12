# Generated by Django 3.2.6 on 2021-08-12 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0002_studentaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=255)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('studentname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelform.studentrecord')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=255)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('classname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelform.classrecord')),
            ],
        ),
    ]
