# Generated by Django 2.1.2 on 2018-11-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_auto_20181111_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='email',
            field=models.EmailField(default='abc@xyz.com', max_length=254),
            preserve_default=False,
        ),
    ]
