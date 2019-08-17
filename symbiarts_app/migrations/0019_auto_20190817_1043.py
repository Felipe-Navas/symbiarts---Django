# Generated by Django 2.2 on 2019-08-17 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symbiarts_app', '0018_merge_20190803_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventaobra',
            name='id_pago',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalleventaobra',
            name='obra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='obra_detalle_venta_obra', to='symbiarts_app.Obra'),
        ),
    ]
