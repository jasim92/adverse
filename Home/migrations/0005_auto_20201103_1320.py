# Generated by Django 3.1.1 on 2020-11-03 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0004_auto_20201024_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='product_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='auther',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
