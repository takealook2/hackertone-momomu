# Generated by Django 3.2.6 on 2021-08-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='유저ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='유저닉네임')),
                ('email', models.EmailField(max_length=100, verbose_name='유저메일')),
                ('password', models.CharField(max_length=100, verbose_name='유저PW')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='마지막수정일')),
            ],
            options={
                'verbose_name': '게시판멤버',
                'verbose_name_plural': '게시판멤버',
                'db_table': 'boardmembers',
            },
        ),
    ]
