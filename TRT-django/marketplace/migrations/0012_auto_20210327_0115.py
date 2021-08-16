# Generated by Django 3.1.7 on 2021-03-27 05:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_auto_20210327_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='album',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='albumimage',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.item'),
        ),
    ]
