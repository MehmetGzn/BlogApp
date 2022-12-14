# Generated by Django 4.1.1 on 2022-09-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="profile_pics/avatar.png", upload_to="profile_pics"
            ),
        ),
    ]
