# Generated by Django 4.2.6 on 2023-10-18 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plane', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('planes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plane.plane')),
            ],
        ),
    ]
