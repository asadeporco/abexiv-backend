# Generated by Django 4.1.2 on 2022-10-18 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('question', '0005_rename_user_id_question_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category'),
        ),
    ]
