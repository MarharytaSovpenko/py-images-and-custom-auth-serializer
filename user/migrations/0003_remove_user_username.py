# Generated by Django 4.1 on 2023-03-11 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_managers_alter_user_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
