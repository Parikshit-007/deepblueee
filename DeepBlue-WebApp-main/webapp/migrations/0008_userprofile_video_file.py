# Generated by Django 4.1.3 on 2023-03-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='video_file',
            field=models.FileField(default='default_value', upload_to='main/videos'),
        ),
    ]
