# Generated by Django 2.1.4 on 2019-02-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notices_noticefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notices',
            name='noticeFile',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
        ),
    ]