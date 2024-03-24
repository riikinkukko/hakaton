# Generated by Django 3.2.16 on 2024-03-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='image_ids',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='video_ids',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='coordinates',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='metadata',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='user_id',
            field=models.IntegerField(blank=True),
        ),
    ]
