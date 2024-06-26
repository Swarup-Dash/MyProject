# Generated by Django 5.0.6 on 2024-06-05 12:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotesVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='myprofile/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(choices=[('PY', 'PYTHON'), ('DJ', 'DJANGO'), ('MS', 'MySql'), ('HM', 'HTML'), ('JV', 'JAVA')], default='PY', max_length=2)),
            ],
        ),
    ]
