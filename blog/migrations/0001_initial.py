# Generated by Django 3.0.5 on 2020-04-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_published', models.DateField()),
                ('blog_data', models.CharField(max_length=5000)),
            ],
        ),
    ]
