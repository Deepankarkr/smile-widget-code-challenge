# Generated by Django 2.0.7 on 2019-04-24 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.PositiveIntegerField(help_text='New Amount as per Schedule')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('Schedule_name', models.CharField(help_text='Black Friday price or 2019 Price', max_length=25)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]