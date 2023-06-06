# Generated by Django 4.1.9 on 2023-06-01 03:57

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('task_id', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('start_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.task')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.student')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('original_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]