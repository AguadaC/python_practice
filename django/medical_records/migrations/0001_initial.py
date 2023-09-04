# Generated by Django 4.1 on 2023-09-04 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('first_consult', models.DateTimeField(auto_now=True)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]