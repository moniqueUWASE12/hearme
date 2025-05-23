# Generated by Django 5.1.7 on 2025-04-06 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_therapist_rename_userinput_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video_url', models.URLField(help_text='URL to the video (e.g., a YouTube link)')),
            ],
        ),
    ]
