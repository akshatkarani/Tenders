# Generated by Django 2.1.2 on 2018-11-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.FileField(upload_to='tender_docs/'),
        ),
    ]