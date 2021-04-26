# Generated by Django 3.1.2 on 2021-04-26 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210425_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postskill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='tasktag',
            name='tag',
        ),
        migrations.AddField(
            model_name='postskill',
            name='skill',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='post_skills', to='posts.skill'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasktag',
            name='skill',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='posts.skill'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postskill',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_skills', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='tasktag',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='posts.task'),
        ),
    ]