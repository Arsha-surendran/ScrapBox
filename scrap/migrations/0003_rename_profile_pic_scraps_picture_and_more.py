# Generated by Django 4.2.6 on 2024-01-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_bids_category_reviews_scraps_userprofile_wishlist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scraps',
            old_name='profile_pic',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pic',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='scraps',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('sold', 'sold')], default='available', max_length=200),
        ),
    ]
