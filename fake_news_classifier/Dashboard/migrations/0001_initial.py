# Generated by Django 3.0.2 on 2020-03-04 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.IntegerField(default=0)),
                ('currency', models.IntegerField(default=1)),
                ('accuracy_perc', models.FloatField(default=0.0)),
                ('contribution', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsVoteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote_count', models.IntegerField(default=0)),
                ('downvote_count', models.IntegerField(default=0)),
                ('downvote', models.ManyToManyField(related_name='downvoted_news', to=settings.AUTH_USER_MODEL)),
                ('upvote', models.ManyToManyField(related_name='upvoted_news', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('news_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('news', models.TextField(default='', unique=True)),
                ('news_link', models.TextField()),
                ('news_img_link', models.TextField(blank=True)),
                ('fake', models.BooleanField(default=False)),
                ('accuracy', models.FloatField(default=0.0)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('news_conn', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_model', to='Dashboard.NewsVoteModel')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_posted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
    ]
