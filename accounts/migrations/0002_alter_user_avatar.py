# Generated by Django 4.2.1 on 2024-01-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default="avatar.svg", null=True, upload_to="profile"
            ),
        ),
    ]
