# Generated by Django 3.2.6 on 2021-10-13 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0007_auto_20211013_0705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='post',
            new_name='postImage',
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.FileField(default='media/default/noimage.png', upload_to='postimages'),
        ),
    ]