# Generated by Django 3.2.4 on 2021-07-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webo_app', '0002_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='fund_no',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='fund_sponsor',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]