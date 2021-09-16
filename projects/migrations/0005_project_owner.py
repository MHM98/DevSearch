# Generated by Django 3.2.6 on 2021-08-18 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_short_intro'),
        ('projects', '0004_project_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
