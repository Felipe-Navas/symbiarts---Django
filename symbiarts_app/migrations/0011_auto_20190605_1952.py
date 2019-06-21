# Generated by Django 2.2 on 2019-06-05 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symbiarts_app', '0010_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='obra',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='symbiarts_app.Categoria'),
            preserve_default=False,
        ),
    ]