# Generated by Django 5.1.1 on 2024-10-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_chatbot_message_chatbot_user_alter_chatbot_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot',
            name='response',
            field=models.TextField(default=''),
        ),
    ]
