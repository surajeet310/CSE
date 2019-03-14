# Generated by Django 2.1.4 on 2018-12-24 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('details', '0002_auto_20181224_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('notice_content', models.CharField(max_length=1000)),
                ('notice_upload_time', models.DateTimeField(auto_now_add=True)),
                ('sem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.Semester')),
            ],
        ),
    ]