# Generated by Django 5.1.7 on 2025-04-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_alter_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='signin_date',
            new_name='signup_date',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fullname',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
