# Generated by Django 2.1.2 on 2018-10-09 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Email_Id', models.EmailField(max_length=20)),
                ('Phone_No', models.CharField(max_length=12)),
                ('Address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('Address2', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1')),
                ('City', models.CharField(max_length=1000)),
                ('Zip_code', models.CharField(max_length=12)),
                ('Country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movietable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Released_date', models.DateTimeField(auto_now_add=True)),
                ('Catogery', models.CharField(max_length=15)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Customertable')),
            ],
        ),
    ]
