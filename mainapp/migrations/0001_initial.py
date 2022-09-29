# Generated by Django 4.1.1 on 2022-09-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('preamble', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Preamble')),
                ('body', models.TextField(verbose_name='Body')),
                ('body_as_markdown', models.BooleanField(default=False, verbose_name='As markdown')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Date of creating')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of editing')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.news')),
            ],
        ),
    ]