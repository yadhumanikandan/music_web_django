# Generated by Django 5.0.4 on 2024-05-04 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_admin', '0005_remove_scale_scale_img_scale_img_guitar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scale',
            old_name='img_guitar',
            new_name='guitar_image',
        ),
        migrations.RenameField(
            model_name='scale',
            old_name='img_keyboard',
            new_name='keyboard_image',
        ),
    ]