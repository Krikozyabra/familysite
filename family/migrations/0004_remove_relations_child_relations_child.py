# Generated by Django 5.0.6 on 2024-06-04 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_alter_relations_child_remove_relations_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relations',
            name='child',
        ),
        migrations.AddField(
            model_name='relations',
            name='child',
            field=models.ManyToManyField(related_name='parent', to='family.familymember'),
        ),
    ]
