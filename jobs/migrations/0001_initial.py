# Generated by Django 4.0.2 on 2022-03-09 10:54

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', ckeditor.fields.RichTextField(default='no description')),
                ('job_type', models.CharField(choices=[('FT', 'Full time'), ('PT', 'Part time'), ('I', 'Internship')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Specialism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('icon', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField(default='no description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='jobs.specialism')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job_Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(choices=[('B', 'Beginner'), ('J', 'Junior'), ('S', 'Senior'), ('P', 'Pro Expert')], max_length=20)),
                ('qualification', models.CharField(choices=[('G', 'Graduation'), ('M', 'Master Degree'), ('BP', 'BPharma'), ('PHD', 'P.H.D')], max_length=20)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='job_specialism',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.specialism'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('icon', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField(default='no description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='jobs.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
