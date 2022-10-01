# Generated by Django 4.1.1 on 2022-10-01 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField(null=True)),
                ('high', models.FloatField(null=True)),
                ('low', models.FloatField(null=True)),
                ('close', models.FloatField(null=True)),
                ('date', models.CharField(max_length=20, null=True)),
                ('volume', models.FloatField(null=True)),
            ],
        ),
    ]
