# Generated by Django 4.0 on 2022-01-18 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0003_article_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='input_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
        ),
    ]