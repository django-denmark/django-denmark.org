# Generated by Django 3.2 on 2021-05-06 13:37
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="logoImage",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="company",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="email",
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name="company",
            name="houseNumber",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="company",
            name="mainContact",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="company",
            name="phoneNumber",
            field=models.CharField(
                blank=True,
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message="fejl", regex="^\\+?1?\\d{9,15}$"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="postalCode",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="company",
            name="region",
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name="company",
            name="streetName",
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name="company",
            name="websiteURL",
            field=models.CharField(max_length=100),
        ),
    ]
