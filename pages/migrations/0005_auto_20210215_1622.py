# Generated by Django 3.0.7 on 2021-02-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_img', models.ImageField(upload_to='images/')),
                ('about_des', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
