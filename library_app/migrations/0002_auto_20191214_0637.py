# Generated by Django 2.2.7 on 2019-12-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField(blank=True)),
                ('pass_word', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='books',
            name='reference_number',
        ),
    ]