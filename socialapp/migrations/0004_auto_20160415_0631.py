# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0003_remove_registration_news_textt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='news_fb_url',
            new_name='fburl',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='news_text',
            new_name='newstext',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='news_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='news_twiter_url',
            new_name='twiterurl',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='news_video_url',
            new_name='video_url',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='news_youtube_url',
            new_name='youtubeurl',
        ),
    ]
