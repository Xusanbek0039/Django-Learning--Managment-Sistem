# Generated by Django 5.0 on 2023-12-26 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0022_auto_20201028_0156"),
        ("enrolls", "0003_auto_20200726_1514"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enrollcouese",
            name="products",
            field=models.ManyToManyField(
                blank=True, related_name="products", to="courses.course"
            ),
        ),
        migrations.AlterField(
            model_name="enrollcouese",
            name="timestamp",
            field=models.DateTimeField(auto_now=True),
        ),
    ]