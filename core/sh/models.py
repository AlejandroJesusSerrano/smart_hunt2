from django.db import models
from datetime import datetime

# Create your models here.
class Brand(models.Model):
  brand = models.CharField(max_length=50, verbose_name = 'Marca')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Regilstro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.brand

  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'
    db_table = 'marca'
    ordering = ['id']

class Dev_Type(models.Model):
  dev_type = models.CharField(max_length = 50, verbose_name = 'Tipo de Dispositivo')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Regilstro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.dev_type

  class Meta:
    verbose_name = 'Tipo de Dispositivo'
    verbose_name_plural = 'Tipos de Dispositivo'
    db_table = 'tipo_de_dispositivo'
    ordering = ['id']

class Model(models.Model):
  dev_type = models.ForeignKey('Dev_Type', related_name = 'models_dev_type', verbose_name = 'Tipo de Dispositivo', on_delete = models.CASCADE)
  brand = models.ForeignKey('Brand', related_name = 'models_brand', on_delete = models.CASCADE)
  model = models.CharField(max_length = 50, verbose_name = 'Modelo')
  image = models.ImageField(upload_to='img_models/%Y/%m/%d', null = True, blank = True, verbose_name = 'Imagen')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.model

  class Meta:
    verbose_name = 'Modelo'
    verbose_name_plural = 'Modelos'
    db_table = 'modelo'
    ordering = ['id']

class Techs(models.Model):
  name = models.CharField(max_length = 75, verbose_name = 'Nombre')
  last_name = models.CharField(max_length = 75, verbose_name = 'Apellido')

  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return f'{self.last_name}, {self.name}'

  class Meta:
    verbose_name = 'Tecnico'
    verbose_name_plural = 'Tecnicos'
    db_table = 'tecnico'
    ordering = ['id']

class Province(models.Model):
  number_id = models.CharField(max_length = 2, verbose_name = 'Numero de Identificación', unique=True)
  province = models.CharField(max_length = 50, verbose_name = 'Provincia', unique=True)
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.province

  class Meta:
    verbose_name = 'Provincia'
    verbose_name_plural = 'Provincias'
    db_table = 'provincias'
    ordering = ['id']

class Location(models.Model):
  province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name = 'Provincia')
  location = models.CharField(max_length = 75, verbose_name = 'Localidad')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.location

  class Meta:
    verbose_name = 'Localidad'
    verbose_name_plural = 'Localidades'
    db_table = 'localidades'
    ordering = ['id']

class Dependency(models.Model):
  description = models.CharField(max_length = 75, verbose_name = 'Dependencia')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = 'Dependencia'
    verbose_name_plural = 'Dependencias'
    db_table = 'dependencia'
    ordering = ['id']

class Edifice(models.Model):
  location = models.ForeignKey(Location, on_delete = models.CASCADE, verbose_name = 'Localidad')
  edifice = models.CharField(max_length = 50, verbose_name = 'Edificio')
  address = models.TextField(verbose_name = 'Domicilio')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return  f'{self.edifice} - {self.address} - {self.location.location} / {self.location.province.province}'

  class Meta:
    verbose_name = 'Edificio'
    verbose_name_plural = 'Edificios'
    db_table = 'edificios'
    ordering = ['id']

class Office(models.Model):

  edifice = models.ForeignKey(Edifice, related_name='office_edifice', verbose_name = 'Edificio', on_delete = models.CASCADE)
  office = models.CharField(max_length = 50, verbose_name = 'Oficina')
  dependency = models.ManyToManyField(Dependency, related_name = 'offices_dependencies', verbose_name = 'Dependencia')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.office

  class Meta:
    verbose_name = 'Officina'
    verbose_name_plural = 'Oficinas'
    db_table = 'oficina'
    ordering = ['id']

class Employee(models.Model):

  ACTIVO = 'ACTIVO'
  MATERNIDAD = 'LICENCIA POR MATERNIDAD'
  LARGO = 'LICENCIA POR LARGO TRATAMIENTO'
  JUBILACION = 'JUBILACION EN TRAMITE'
  BAJA = 'BAJA O RETIRADO'

  STATUS_CHOICES = {
    (ACTIVO, 'ACTIVO'),
    (MATERNIDAD, 'LICENCIA POR MATERNIDAD'),
    (LARGO, 'LICENCIA POR LARGO TRATAMIENTO'),
    (JUBILACION, 'JUBILACION EN TRAMITE'),
    (BAJA, 'BAJA O RETIRADO')
  }

  employee_name = models.CharField(max_length = 50, verbose_name = 'Nombre del Empleado')
  employee_last_name = models.CharField(max_length = 50, verbose_name = 'Apellido')
  cuil = models.CharField(max_length = 11, verbose_name = 'cuil')
  status = models.CharField(max_length = 30, choices = STATUS_CHOICES, default = ACTIVO, verbose_name = 'Estado')
  user_pc = models.CharField(max_length = 11, verbose_name = 'Nombre de Usuario')
  office = models.ForeignKey(Office, related_name = 'employee_office', verbose_name = 'Oficina',  on_delete = models.CASCADE,)
  avatar = models.ImageField(upload_to='img_avatars/%Y/%m/%d', null = True, blank = True, verbose_name = 'Avatar')
  dependency = models.ForeignKey(Dependency, related_name = 'employee_dependency', verbose_name= 'Dependencia',  on_delete = models.CASCADE,)
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return f'{self.employee_last_name}, {self.employee_name} - {self.cuil} - {self.office.office} - {self.status}'

  def employee_full_name(self):
    return f'{self.employee_last_name}, {self.employee_name}'

  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    db_table = 'empleados'
    ordering = ['id']


class ImgPrinterDevice(models.Model):
  USB = 'USB'
  RED = 'RED'

  CONNECTION_TYPE_CHOICES = [
    (USB, 'USB'),
    (RED, 'RED')
  ]

  ip = models.CharField(max_length = 15, verbose_name = 'Direccion Ip', null = True, blank = True)
  last_review = models.DateField(verbose_name = 'Última Revision')
  connection_type = models.CharField(max_length = 3, choices = CONNECTION_TYPE_CHOICES, default = RED, verbose_name = 'Tipo de Conexion' )
  tech = models.ForeignKey(Techs, related_name = 'img_printer_tech', verbose_name = 'Técnico', on_delete = models.CASCADE)
  model = models.ForeignKey(Model, related_name = 'img_printer_model', verbose_name = 'Modelo', on_delete = models.CASCADE)
  serial_p = models.CharField(max_length = 20, verbose_name = 'Número de Serie')
  employee = models.ForeignKey(Employee, related_name = 'img_printer_employee', verbose_name = 'Empleado', on_delete = models.CASCADE)
  active = models.BooleanField(default=1)
  operational = models.BooleanField(default=1)
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return f'{self.model.dev_type} - {self.brand.brand} - {self.model.model} - {self.serial_p} - {self.ip}'

  def computer_data(self):
    return f'Marca: {self.model.brand}, Ip: {self.ip}, Modelo: {self.model.model} S/N°: {self.serial_p}'

  class Meta:
    verbose_name = 'Impresor y Scanner'
    verbose_name_plural = 'Impresoras y Scanners'
    db_table = 'impresoras_scanners'
    ordering = ['id']

class Computer(models.Model):
  ip = models.CharField(max_length = 15, verbose_name = 'Direccion Ip')
  pc_net_name = models.CharField(max_length = 11, verbose_name = 'Nombre de Equipo en la Red')
  last_review = models.DateField(verbose_name = 'Última Revision')
  tech = models.ForeignKey(Techs, related_name = 'computer_tech', verbose_name = 'Técnico', on_delete = models.CASCADE)
  model = models.ForeignKey(Model, related_name = 'computer_model', verbose_name = 'Modelo', on_delete = models.CASCADE)
  serial_c = models.CharField(max_length = 20, verbose_name = 'Número de Serie')
  employee = models.ForeignKey(Employee, related_name = 'computer_employee', verbose_name = 'Empleado', on_delete = models.CASCADE)
  printer = models.ManyToManyField(ImgPrinterDevice, related_name='computers', verbose_name='Impresoras')
  operational = models.BooleanField(default=1)
  active = models.BooleanField(default=1)
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return f'{self.model.brand.brand} - {self.model.model} - {self.serial_c} - {self.ip} - {self.pc_net_name} - {self.employee.employee_last_name}, {self.employee.employee_name}'

  def computer_data(self):
    return f'Marca: {self.model.brand}, Ip: {self.ip}, Nombre Pc: {self.pc_net_name}, Modelo: {self.model.model}, S/N°: {self.serial_c}'

  class Meta:
    verbose_name = 'Computadora'
    verbose_name_plural = 'Computadoras'
    db_table = 'computadoras'
    ordering = ['id']

class Monitor(models.Model):
  operational = models.BooleanField(default=1)
  active = models.BooleanField(default=1)
  computer_assigned = models.ForeignKey(Computer, related_name = 'monitor_computer', verbose_name = 'Computadora Asignada', on_delete = models.CASCADE, null = True, blank = True)
  last_review = models.DateField(verbose_name = 'Última Revision')
  tech = models.ForeignKey(Techs, related_name = 'monitor_tech', verbose_name = 'Técnico', on_delete = models.CASCADE)
  model = models.ForeignKey(Model, related_name = 'monitor_model', verbose_name = 'Modelo', on_delete = models.CASCADE)
  serial_m = models.CharField(max_length = 20, verbose_name = 'Número de Serie')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return f'{self.model.brand.brand} - {self.model.model} - {self.computer_assigned}'

  def monitor_data(self):
    return f'Marca: {self.model.brand}, Modelo: {self.model.model}, S/N°: {self.serial_m}'

  class Meta:
    verbose_name = 'Monitor'
    verbose_name_plural = 'Monitores'
    db_table = 'monitores'
    ordering = ['id']

class Peripherals(models.Model):
  operational = models.BooleanField(default=1)
  active = models.BooleanField(default=1)
  computer_assigned = models.ForeignKey(Computer, related_name = 'peripherals_computer', verbose_name = 'Computadora Asignada', on_delete = models.CASCADE, null = True, blank = True)
  last_review = models.DateField(verbose_name = 'Última Revision')
  model = models.ForeignKey(Model, related_name = 'peripherals_model', verbose_name = 'Modelo', on_delete = models.CASCADE)
  serial_per = models.CharField(max_length = 20, verbose_name = 'Número de Serie')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return f'{self.model.dev_type} - {self.model.brand.brand} - {self.model.model} - {self.serial_k} - {self.computer_assigned}'

  def monitor_data(self):
    return f'Marca: {self.model.brand}, Modelo: {self.model.model}, S/N°: {self.serial_k}'

  class Meta:
    verbose_name = 'Periferico'
    verbose_name_plural = 'Perifericos'
    db_table = 'perifericos'
    ordering = ['id']

