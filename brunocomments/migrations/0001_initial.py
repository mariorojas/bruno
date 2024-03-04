# Generated by Django 4.2.7 on 2023-11-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('comment', models.TextField(max_length=3000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]