# Generated by Django 5.0.2 on 2024-05-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh', '0009_alter_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('LICENCIA POR LARGO TRATAMIENTO', 'LICENCIA POR LARGO TRATAMIENTO'), ('BAJA O RETIRADO', 'BAJA O RETIRADO'), ('LICENCIA POR MATERNIDAD', 'LICENCIA POR MATERNIDAD'), ('ACTIVO', 'ACTIVO'), ('JUBILACION EN TRAMITE', 'JUBILACION EN TRAMITE')], default='ACTIVO', max_length=30, verbose_name='Estado'),
        ),
    ]
