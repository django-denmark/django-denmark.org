# Generated by Django 2.0.3 on 2018-03-17 23:21

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapentry',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
    ]
