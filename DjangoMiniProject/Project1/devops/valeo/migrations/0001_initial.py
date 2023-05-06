# Generated by Django 4.2.1 on 2023-05-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, null=True)),
                ('idd', models.IntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('salary', models.FloatField(null=True)),
                ('creationTime', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateTime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]