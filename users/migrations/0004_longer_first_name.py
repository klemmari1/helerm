# Generated by Django 3.1.5 on 2021-01-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_longer_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]