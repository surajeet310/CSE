# Generated by Django 2.1.4 on 2019-02-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notices',
            name='noticeFile',
            field=models.ImageField(default='default.png', upload_to='media/'),
        ),
    ]
