# Generated by Django 3.2.3 on 2021-05-17 02:58

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('content', '0002_alter_content_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
