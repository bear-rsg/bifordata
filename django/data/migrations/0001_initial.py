# Generated by Django 3.2.8 on 2021-10-18 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('filepath', models.TextField(unique=True)),
                ('is_public', models.BooleanField(default=True)),
                ('slug', models.SlugField()),
                ('parent_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.folder')),
            ],
            options={
                'ordering': ['name', 'id'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('extension', models.CharField(blank=True, max_length=255, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('slug', models.SlugField()),
                ('parent_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.folder')),
            ],
            options={
                'ordering': ['name', 'id'],
            },
        ),
    ]
