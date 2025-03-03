# Generated by Django 5.0.6 on 2024-06-04 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='deathDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
