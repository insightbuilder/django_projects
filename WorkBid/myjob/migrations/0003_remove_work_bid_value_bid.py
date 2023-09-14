# Generated by Django 4.0.7 on 2023-08-28 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myjob', '0002_work_bid_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='bid_value',
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('bid_value', models.IntegerField(default=0)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myjob.work')),
            ],
        ),
    ]
