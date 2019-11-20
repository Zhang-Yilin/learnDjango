# Generated by Django 2.2.6 on 2019-10-20 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_blog_read_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_time', models.DateTimeField(auto_now_add=True)),
                ('read_blog', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog')),
                ('reader', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
