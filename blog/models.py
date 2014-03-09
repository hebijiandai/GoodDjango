# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Mark(models.Model):
    mark = models.CharField('标签', max_length=50)
    license = models.CharField('证书', max_length=50)

    def __unicode__(self):
        return unicode(self.mark)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'


class Qualification(models.Model):
    qualification = models.CharField('资质', max_length=50)
    license = models.CharField('证书', max_length=50)
    charactor = models.CharField('性格', max_length=50)
    level = models.SmallIntegerField('级别')

    def __unicode__(self):
        return unicode(self.qualification)

    class Meta:
        verbose_name = '资质'
        verbose_name_plural = '资质'

@python_2_unicode_compatible
class Author(models.Model):
    author = models.CharField('作者', max_length=50)
    title = models.CharField('标题', max_length=150)
    qualification = models.ForeignKey(Qualification)
    mark = models.ManyToManyField(Mark)
    blog = models.TextField('博客内容')
    time = models.DateField('写作日期')

    def __str__(self):
        return self.author

    # def __unicode__(self):
    #     return unicode(self.author)

    class Meta:
        ordering = ['time']
        verbose_name = '相关博客'
        verbose_name_plural = '相关博客'


class Objectattribution(models.Model):
    attribution = models.CharField('归属', max_length=50)
    place = models.PositiveIntegerField('地点', default=0)

    def __unicode__(self):
        return unicode(self.attribution)

    class Meta:
        verbose_name='物品归属'
        verbose_name_plural='物品归属'


class Material(models.Model):
    material = models.CharField('material', max_length=50)
    Autoignition_temperature = models.SmallIntegerField('Autoignition temperature', max_length=50)
    Binary_phase_diagram = models.CharField('Binary phase diagram', max_length=50)
    Boiling_point = models.CharField('Boiling point', max_length=50)
    Coefficient_of_thermal_expansion = models.CharField('Coefficient of thermal expansion', max_length=50)
    Critical_temperature = models.SmallIntegerField('Critical temperature', max_length=50)
    Curie_point = models.CharField('Curie point', max_length=50)
    Emissivity = models.CharField('Emissivity', max_length=50)
    Eutectic_point = models.CharField('Eutectic point', max_length=50)
    Flammability = models.CharField('Flammability', max_length=50)
    Flash_point = models.CharField('Flash point', max_length=50)
    Glass_transition_temperature = models.CharField('Glass transition temperature', max_length=50)
    Heat_of_fusion = models.CharField('Heat of fusion', max_length=50)
    Heat_of_vaporization = models.CharField('Heat of vaporization', max_length=50)
    Inversion_temperature = models.CharField('Inversion temperature', max_length=50)
    Melting_point = models.CharField('Melting point', max_length=50)
    Phase_diagram = models.CharField('Phase diagram', max_length=50)
    Pyrophoricity = models.CharField('Pyrophoricity', max_length=50)
    Solidus = models.CharField('Solidus', max_length=50)
    Specific_heat = models.CharField('Specific heat', max_length=50)
    Thermal_conductivity = models.CharField('Thermal conductivity', max_length=50)
    Thermal_diffusivity = models.CharField('Thermal diffusivity', max_length=50)
    Thermal_expansion = models.CharField('Thermal expansion', max_length=50)
    Seebeck_coefficient = models.CharField('Seebeck coefficient', max_length=50)
    Triple_point = models.CharField('Triple point', max_length=50)
    Vapor_pressure = models.CharField('Vapor pressure', max_length=50)
    Vicat_softening_point = models.CharField('Vicat softening point', max_length=50)

    def __unicode__(self):
        return unicode(self.material)

    class Meta:
        verbose_name_plural = '物品材料构成'
        verbose_name = '物品材料构成'


class Myobject(models.Model):
    object = models.CharField('物品', max_length=50)
    content = models.CharField('产品内容', max_length=50)
    attribution = models.ForeignKey(Objectattribution)
    material = models.ForeignKey(Material)
    order = models.PositiveIntegerField('顺序', default=0)
    bontime = models.DateField('生产日期')

    def __unicode__(self):
        return unicode(self.object)

    class Meta:
        verbose_name_plural = '物品'
        verbose_name = '物品'


class Adress(models.Model):
    receivename = models.CharField('收件姓名', max_length=50)
    adress = models.TextField('收件地址')

    def __unicode__(self):
        return unicode(self.receivename)

    class Meta:
        verbose_name = '收件地址'
        verbose_name_plural = '收件地址'


class CustomView(models.Model):
    pass
