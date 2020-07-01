# Generated by Django 3.0.7 on 2020-06-30 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_newsletter_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='content',
            field=models.FileField(default=django.utils.timezone.now, upload_to='templates/'),
            preserve_default=False,
        ),
    ]