# Generated by Django 5.1.1 on 2024-10-09 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='message',
            field=models.TextField(default='Default message'),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatbot',
            name='response',
            field=models.TextField(),
        ),
    ]
