# Generated by Django 2.0.1 on 2018-01-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180108_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('WW', 'Wood Working'), ('SP', 'Sports')], default=None, max_length=2),
        ),
    ]
