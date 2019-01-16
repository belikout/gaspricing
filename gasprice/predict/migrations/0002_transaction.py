# Generated by Django 2.1.3 on 2019-01-11 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gasprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('difficulty', models.DecimalField(decimal_places=2, max_digits=8)),
                ('avegasprice', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
