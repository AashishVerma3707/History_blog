# Generated by Django 4.0 on 2022-01-16 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
