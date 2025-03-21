# Generated by Django 5.1.6 on 2025-02-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('PROG', 'Programming Languages'), ('FRAM', 'Frameworks'), ('TOOL', 'Tools & Technologies'), ('SOFT', 'Soft Skills')], max_length=4)),
                ('proficiency', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_pics/')),
                ('project_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('date_completed', models.DateField()),
                ('technologies', models.ManyToManyField(to='portfolio.skill')),
            ],
            options={
                'ordering': ['-date_completed'],
            },
        ),
    ]
