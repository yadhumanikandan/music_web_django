# Generated by Django 5.0.4 on 2024-09-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_admin', '0008_alter_scale_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chord', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('keyboard_image', models.ImageField(default='x', upload_to='scales/keyboard')),
                ('guitar_image', models.ImageField(default='x', upload_to='scales/guitar')),
            ],
        ),
    ]