# Generated by Django 3.0.5 on 2020-04-23 17:25

import app.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='tmp/', validators=[app.validators.is_valid_size, app.validators.is_mp3])),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('source_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='app.SourceFile')),
            ],
        ),
    ]