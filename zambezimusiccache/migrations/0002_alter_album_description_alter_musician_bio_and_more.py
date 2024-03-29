# Generated by Django 4.1.6 on 2023-04-29 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zambezimusiccache', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zambezimusiccache.album'),
        ),
        migrations.AlterField(
            model_name='track',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
