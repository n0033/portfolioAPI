# Generated by Django 3.1.7 on 2021-04-13 06:58

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description_1', models.TextField()),
                ('description_2', models.TextField()),
                ('description_3', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 'python'), (1, 'django'), (2, 'djangorestframwork'), (3, 'javascript'), (4, 'react'), (5, 'html'), (6, 'css')], max_length=13),
        ),
    ]
