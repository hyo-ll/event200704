# Generated by Django 3.0.8 on 2020-07-01 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobetsu', '0002_auto_20200702_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='choice_member',
            field=models.CharField(default='神楽 美佳', max_length=30),
            preserve_default=False,
        ),
    ]