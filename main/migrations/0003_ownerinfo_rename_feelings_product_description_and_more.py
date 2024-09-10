# Generated by Django 5.1.1 on 2024-09-09 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_moodentry_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='feelings',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='mood',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='mood_intensity',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='time',
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(default='In Stock', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(default='No discount', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='images/default.avif', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]