# Generated by Django 5.0.7 on 2024-08-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('Stat', 'Statistical')], default='custom', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]