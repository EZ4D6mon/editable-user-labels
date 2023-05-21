# Generated by Django 4.2.1 on 2023-05-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.tag'),
        ),
    ]
