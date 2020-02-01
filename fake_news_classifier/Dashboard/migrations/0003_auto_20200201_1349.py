# Generated by Django 3.0.2 on 2020-02-01 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_newsvotemodel_news_conn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsvotemodel',
            name='news_conn',
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='news_conn',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='news_model', to='Dashboard.NewsVoteModel'),
        ),
    ]
