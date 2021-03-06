# Generated by Django 2.2 on 2019-07-01 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('symbiarts_app', '0013_auto_20190622_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VentaObra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('metodo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='symbiarts_app.MetodoPago')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVentaObra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_obra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cantidad_obra', models.IntegerField()),
                ('obra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='symbiarts_app.Obra')),
                ('venta_obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_venta_obra', to='symbiarts_app.VentaObra')),
            ],
        ),
    ]
