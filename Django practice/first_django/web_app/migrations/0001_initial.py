# Generated by Django 5.1.7 on 2025-04-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0)),
                ('age', models.IntegerField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
