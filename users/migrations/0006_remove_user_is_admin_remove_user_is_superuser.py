# Generated by Django 4.2.10 on 2024-02-28 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_is_staff_user_is_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]
