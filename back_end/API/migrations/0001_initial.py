# Generated by Django 3.0.4 on 2020-04-29 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.TextField(max_length=200)),
                ('rating', models.FloatField(max_length=200)),
                ('image', models.TextField()),
                ('description', models.TextField()),
                ('ref', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Category')),
            ],
        ),
    ]