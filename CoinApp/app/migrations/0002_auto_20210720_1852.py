# Generated by Django 3.2.5 on 2021-07-20 16:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PercentageAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.alert')),
                ('timeframe', models.DurationField()),
                ('percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('direction', models.CharField(choices=[('U', 'Up'), ('D', 'Down')], max_length=1)),
            ],
            bases=('app.alert',),
        ),
        migrations.CreateModel(
            name='ValueAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.alert')),
                ('value', models.DecimalField(decimal_places=10, max_digits=30)),
                ('crypto', models.CharField(max_length=3)),
                ('currency', models.CharField(max_length=3)),
                ('direction', models.CharField(choices=[('A', 'Above'), ('B', 'Below')], max_length=1)),
            ],
            bases=('app.alert',),
        ),
        migrations.AddField(
            model_name='alert',
            name='activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
    ]