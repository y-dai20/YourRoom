# Generated by Django 3.2.5 on 2023-02-25 02:56

import base.models.functions
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20230224_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.CharField(default=base.models.functions.create_id, editable=False, max_length=30, primary_key=True, serialize=False)),
                ('tag1', models.CharField(blank=True, default='', max_length=15)),
                ('tag2', models.CharField(blank=True, default='', max_length=15)),
                ('tag3', models.CharField(blank=True, default='', max_length=15)),
                ('tag4', models.CharField(blank=True, default='', max_length=15)),
                ('tag5', models.CharField(blank=True, default='', max_length=15)),
                ('tag6', models.CharField(blank=True, default='', max_length=15)),
                ('tag7', models.CharField(blank=True, default='', max_length=15)),
                ('tag8', models.CharField(blank=True, default='', max_length=15)),
                ('tag9', models.CharField(blank=True, default='', max_length=15)),
                ('tag10', models.CharField(blank=True, default='', max_length=15)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tag'),
        ),
        migrations.AddField(
            model_name='room',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tag'),
        ),
    ]
