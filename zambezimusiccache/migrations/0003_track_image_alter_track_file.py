# Generated by Django 4.1.6 on 2023-04-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zambezimusiccache', '0002_alter_album_description_alter_musician_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='track',
            name='file',
            field=models.FileField(upload_to='music/'),
        ),
    ]
