# Generated by Django 5.0.7 on 2024-09-08 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Blog_App", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="database",
            name="image",
            field=models.ImageField(null=True, upload_to="images_folder"),
        ),
    ]
