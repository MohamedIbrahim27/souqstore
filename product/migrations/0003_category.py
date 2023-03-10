# Generated by Django 3.2 on 2022-11-06 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20221106_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=50)),
                ('CATDes', models.TextField()),
                ('CATImg', models.ImageField(upload_to='category')),
                ('CATParent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='')),
            ],
        ),
    ]
