# Generated by Django 4.1 on 2022-09-01 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_question_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user_id',
            new_name='user',
        ),
    ]
