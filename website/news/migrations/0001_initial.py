# Generated by Django 3.0.2 on 2020-03-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
