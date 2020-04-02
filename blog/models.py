# coding:utf-8
from django.db import models
import datetime
import os


class Mark(models.Model):
    mark = models.CharField('标签_tag', max_length=50)
    license = models.CharField('证书', max_length=50)

    def __str__(self):
        return self.mark

    class Meta:
        ordering = ['mark']
        verbose_name = '文章的标签不合理'
        verbose_name_plural = '文章的标签不合理'

    def __unicode__(self):
        return self.mark

# 增加user，比照账户的名字，类似access数据库的处理


class Qualification(models.Model):
    qualification = models.CharField('资质', max_length=50)
    license = models.CharField('证书', max_length=50)
    charactor = models.CharField('性格', max_length=50)
    level = models.SmallIntegerField('级别')
    user = models.CharField('填写人', max_length=50)

    def __str__(self):
        return self.qualification

    class Meta:
        verbose_name = '资质安排'
        verbose_name_plural = '资质安排'

    def __unicode__(self):
        return self.qualification

# 自定义Filefield，Imaginfiled的路径名


def get_photo_path(instance, filename):
    '''dynamic upload path'''
    mydate = datetime.datetime.now().strftime('%Y%m')
    # 分离文件名和文件扩展名
    fname, ext = os.path.splitext(filename)
    return u'./UploadFiles/%s/%s-%s-%s-第%s号文件%s' % (instance.projectname, instance.author,
                                                    instance.title, mydate, instance.id, ext.lower())


class Author(models.Model):
    author = models.CharField('作者', max_length=50)
    title = models.CharField('标题', max_length=150)
    qualification = models.ForeignKey(Qualification)
    mark = models.ManyToManyField(Mark)
    myfile = models.FileField('我的文件', upload_to=get_photo_path)
    projectname = models.CharField('项目备注', max_length=50)
    frequency = models.SmallIntegerField('提交频次', max_length=10)
    blog = models.TextField('博客内容')
    time = models.DateField('写作日期')

    def __str__(self):
        return self.author
    # 如果文件同名，则替换，删除掉原来的

    def save(self, *args, **kwargs):
        # delete old file whe n replacing by updating the file
        try:
            this = Author.objects.get(id=self.id)
            # 只比较了文件名，很好！
            if this.myfile != self.myfile:
                this.myfile.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(Author, self).save(*args, **kwargs)

    class Meta:
        ordering = ['time']
        verbose_name = '相关的BLOG'
        verbose_name_plural = '相关的BLOG'

    def __unicode__(self):
        return self.author


class Objectattribution(models.Model):
    attribution = models.CharField('归属', max_length=50)
    place = models.PositiveIntegerField('地点', default=0)

    def __str__(self):
        return self.attribution

    class Meta:
        verbose_name = '物品归属HAHAHA'
        verbose_name_plural = '物品归属'

    def __unicode__(self):
        return self.attribution


class Material(models.Model):
    material = models.CharField('材料名称', max_length=50)
    Autoignition_temperature = models.SmallIntegerField(
        '自燃温度', max_length=50)
    Binary_phase_diagram = models.CharField(
        '二进制相图', max_length=50)
    Boiling_point = models.CharField('沸点', max_length=50)
    Coefficient_of_thermal_expansion = models.CharField(
        '热膨胀系数', max_length=50)
    Critical_temperature = models.SmallIntegerField(
        '临界温度', max_length=50)
    Curie_point = models.CharField('居里点', max_length=50)
    Emissivity = models.CharField('发射率', max_length=50)
    Eutectic_point = models.CharField('共晶点', max_length=50)
    Flammability = models.CharField('可燃性', max_length=50)
    Flash_point = models.CharField('闪点', max_length=50)
    Glass_transition_temperature = models.CharField(
        '相图', max_length=50)
    Heat_of_fusion = models.CharField('融合热', max_length=50)
    Heat_of_vaporization = models.CharField(
        '汽化热', max_length=50)
    Inversion_temperature = models.CharField(
        '反转温度', max_length=50)
    Melting_point = models.CharField('熔点', max_length=50)
    Phase_diagram = models.CharField('相图', max_length=50)
    Pyrophoricity = models.CharField('发火性', max_length=50)
    Solidus = models.CharField('固相线', max_length=50)
    Specific_heat = models.CharField('比热', max_length=50)
    Thermal_conductivity = models.CharField(
        '导热系数', max_length=50)
    Thermal_diffusivity = models.CharField(
        '热扩散系数', max_length=50)
    Thermal_expansion = models.CharField('热膨胀', max_length=50)
    Seebeck_coefficient = models.CharField(
        '塞贝克系数', max_length=50)
    Triple_point = models.CharField('三点', max_length=50)
    Vapor_pressure = models.CharField('蒸汽压力', max_length=50)
    Vicat_softening_point = models.CharField(
        '维卡软化点', max_length=50)

    def __str__(self):
        return self.material

    class Meta:
        verbose_name_plural = '物品材料构成'
        verbose_name = '物品材料构成'

    def __unicode__(self):
        return self.material


class Myobject(models.Model):
    object = models.CharField('生产物品', max_length=50)
    content = models.CharField('产品内容', max_length=50)
    attribution = models.ForeignKey(Objectattribution)
    material = models.ForeignKey(Material)
    order = models.PositiveIntegerField('顺序', default=0)
    bontime = models.DateField('生产日期')

    def __str__(self):
        return self.object

    class Meta:
        verbose_name_plural = '我们物品'
        verbose_name = '我们物品'

    def __unicode__(self):
        return self.object


class Adress(models.Model):
    receivename = models.CharField('收件姓名', max_length=50)
    adress = models.TextField('收件地址')

    def __str__(self):
        return self.receivename

    class Meta:
        verbose_name = '收件地址'
        verbose_name_plural = '收件地址'

    def __unicode__(self):
        return self.receivename


class CustomView(models.Model):
    pass
