# Generated by Django 3.1.6 on 2021-02-21 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_auto_20210221_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangoapp.sample'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_number',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_number', models.IntegerField()),
                ('message', models.CharField(max_length=25)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djangoapp.sample')),
            ],
        ),
    ]
