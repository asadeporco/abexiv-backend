# Generated by Django 4.1.1 on 2022-10-07 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_rename_user_id_question_user'),
        ('answer', '0003_rename_user_id_answer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='question.question'),
            preserve_default=False,
        ),
    ]
