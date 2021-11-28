# Generated by Django 3.2.9 on 2021-11-27 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=250)),
                ('detail', models.CharField(max_length=4095)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]