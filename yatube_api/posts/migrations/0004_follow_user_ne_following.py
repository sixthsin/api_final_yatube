# Generated by Django 4.2.15 on 2024-08-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_comment_id_alter_follow_id_alter_group_id_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', models.F('following')), _negated=True), name='user_ne_following'),
        ),
    ]
