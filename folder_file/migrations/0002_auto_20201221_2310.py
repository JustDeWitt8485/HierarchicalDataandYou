# Generated by Django 3.1.4 on 2020-12-21 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder_file', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FolderFile',
            new_name='File',
        ),
    ]