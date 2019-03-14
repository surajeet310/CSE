# Generated by Django 2.1.4 on 2019-02-18 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('details', '0002_auto_20181224_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=100)),
                ('course_file', models.FileField(upload_to='')),
                ('sem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.Semester')),
            ],
        ),
    ]