# Generated by Django 4.2.10 on 2024-02-28 14:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('floor_count', models.IntegerField(default=0, null=True)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('floor', models.IntegerField(db_index=True, default=0)),
                ('number', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserOffice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('Office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.office')),
            ],
            options={
                'ordering': ['created'],
                'abstract': False,
            },
        ),
    ]
