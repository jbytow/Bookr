# Generated by Django 4.1.7 on 2023-03-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0, help_text="user's rating"),
        ),
        migrations.AlterField(
            model_name='bookcontributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='Role of the contributor'),
        ),
    ]
