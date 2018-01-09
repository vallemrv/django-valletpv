# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-03 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arqueocaja',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cambio', models.FloatField(db_column='Cambio')),
                ('descuadre', models.FloatField(db_column='Descuadre')),
            ],
            options={
                'db_table': 'arqueocaja',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Camareros',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('apellidos', models.CharField(db_column='Apellidos', max_length=100)),
                ('email', models.CharField(db_column='Email', max_length=50)),
                ('pass_field', models.CharField(db_column='Pass', max_length=100)),
                ('activo', models.IntegerField(db_column='Activo')),
            ],
            options={
                'db_table': 'camareros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cierrecaja',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ticketcom', models.IntegerField(db_column='TicketCom')),
                ('ticketfinal', models.IntegerField(db_column='TicketFinal')),
                ('fecha', models.CharField(db_column='Fecha', max_length=10)),
                ('hora', models.CharField(db_column='Hora', max_length=5)),
            ],
            options={
                'db_table': 'cierrecaja',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('color', models.CharField(db_column='Color', max_length=20)),
                ('rgb', models.CharField(db_column='RGB', max_length=11)),
            ],
            options={
                'db_table': 'colores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=100)),
            ],
            options={
                'db_table': 'cuentas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Efectivo',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('can', models.IntegerField(db_column='Can')),
                ('moneda', models.DecimalField(db_column='Moneda', decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'efectivo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Familias',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=40)),
                ('tipo', models.CharField(db_column='Tipo', max_length=6)),
                ('numtapas', models.IntegerField(db_column='NumTapas')),
            ],
            options={
                'db_table': 'familias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=50)),
                ('importe', models.DecimalField(db_column='Importe', decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'gastos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historialnulos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hora', models.CharField(db_column='Hora', max_length=5)),
                ('motivo', models.CharField(db_column='Motivo', max_length=100)),
            ],
            options={
                'db_table': 'historialnulos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HorarioUsr',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hora_ini', models.CharField(db_column='Hora_ini', max_length=5)),
                ('hora_fin', models.CharField(db_column='Hora_fin', max_length=5)),
            ],
            options={
                'db_table': 'horario_usr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Infmesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(db_column='UID', max_length=100, unique=True)),
                ('fecha', models.CharField(db_column='Fecha', max_length=10)),
                ('hora', models.CharField(db_column='Hora', max_length=5)),
                ('ref', models.CharField(db_column='Ref', max_length=50)),
                ('numcopias', models.IntegerField(db_column='NumCopias')),
            ],
            options={
                'db_table': 'infmesa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lineaspedido',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idart', models.IntegerField(db_column='IDArt')),
                ('estado', models.CharField(db_column='Estado', max_length=1)),
                ('precio', models.DecimalField(db_column='Precio', decimal_places=2, max_digits=6)),
                ('nombre', models.CharField(db_column='Nombre', max_length=70)),
            ],
            options={
                'db_table': 'lineaspedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50, unique=True)),
                ('orden', models.IntegerField(db_column='Orden')),
            ],
            options={
                'db_table': 'mesas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesasabiertas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'mesasabiertas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesaszona',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'mesaszona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idsub', models.IntegerField(db_column='IDSub')),
                ('fecha', models.CharField(db_column='Fecha', max_length=10)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=100)),
                ('idsub_pago', models.IntegerField(db_column='IDSub_pago')),
            ],
            options={
                'db_table': 'movimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hora', models.CharField(db_column='Hora', max_length=5)),
                ('idcam', models.IntegerField(db_column='IDCam')),
            ],
            options={
                'db_table': 'pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receptores',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=40)),
                ('nomimp', models.CharField(db_column='nomImp', max_length=40)),
            ],
            options={
                'db_table': 'receptores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Secciones',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('color', models.CharField(db_column='Color', max_length=20)),
                ('rgb', models.CharField(db_column='RGB', max_length=11)),
                ('orden', models.IntegerField(db_column='Orden')),
            ],
            options={
                'db_table': 'secciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeccionesCom',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=11)),
            ],
            options={
                'db_table': 'secciones_com',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servidos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'servidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subcuentas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('apodo', models.CharField(db_column='Apodo', max_length=100)),
                ('idcuenta', models.IntegerField(db_column='IDCuenta')),
                ('notas', models.TextField(db_column='Notas')),
                ('tipo', models.CharField(db_column='Tipo', max_length=5)),
            ],
            options={
                'db_table': 'subcuentas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subteclas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('idtecla', models.IntegerField(db_column='IDTecla')),
                ('incremento', models.DecimalField(db_column='Incremento', decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'subteclas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sugerencias',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idtecla', models.IntegerField(db_column='IDTecla')),
                ('sugerencia', models.CharField(db_column='Sugerencia', max_length=50)),
            ],
            options={
                'db_table': 'sugerencias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('modificado', models.CharField(db_column='Modificado', max_length=25)),
                ('tabla', models.CharField(db_column='Tabla', max_length=50)),
                ('args', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sync',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teclas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('p1', models.DecimalField(db_column='P1', decimal_places=2, max_digits=6)),
                ('p2', models.DecimalField(db_column='P2', decimal_places=2, max_digits=6)),
                ('orden', models.IntegerField(db_column='Orden')),
                ('tag', models.CharField(db_column='Tag', max_length=100)),
                ('ttf', models.CharField(db_column='TTF', max_length=50)),
            ],
            options={
                'db_table': 'teclas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teclascom',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('orden', models.IntegerField(db_column='Orden')),
            ],
            options={
                'db_table': 'teclascom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teclaseccion',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'teclaseccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('fecha', models.CharField(db_column='Fecha', max_length=10)),
                ('idcam', models.IntegerField(db_column='IDCam')),
                ('hora', models.CharField(db_column='Hora', max_length=5)),
                ('entrega', models.DecimalField(db_column='Entrega', decimal_places=2, max_digits=6)),
                ('uid', models.CharField(db_column='UID', max_length=100)),
                ('mesa', models.CharField(db_column='Mesa', max_length=40)),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticketlineas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'ticketlineas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('apellido', models.CharField(db_column='Apellido', max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('pass_field', models.CharField(db_column='Pass', max_length=11)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zonas',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50, unique=True)),
                ('tarifa', models.IntegerField(db_column='Tarifa')),
                ('color', models.CharField(db_column='Color', max_length=50)),
                ('rgb', models.CharField(db_column='RGB', max_length=50)),
            ],
            options={
                'db_table': 'zonas',
                'managed': False,
            },
        ),
    ]
