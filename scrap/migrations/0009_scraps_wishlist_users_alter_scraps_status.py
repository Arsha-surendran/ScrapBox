# Generated by Django 4.2.6 on 2024-01-22 05:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrap', '0008_alter_scraps_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraps',
            name='wishlist_users',
            field=models.ManyToManyField(blank=True, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scraps',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('sold', 'sold')], default='available', max_length=200),
        ),
    ]
