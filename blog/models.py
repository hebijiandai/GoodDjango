# coding:utf-8
from django.db import models


class Mark(models.Model):
    mark = models.CharField('标签', max_length=50)
    license = models.CharField('证书', max_length=50)

    def __unicode__(self):
        return unicode(self.mark)

        # class Meta:
        #     verbose_name = '文章标签'
        #     verbose_name_plural = '文章标签'


class Qualification(models.Model):
    qualification = models.CharField('资质', max_length=50)
    license = models.CharField('证书', max_length=50)
    charactor = models.CharField('性格', max_length=50)
    level = models.SmallIntegerField('级别')


    def __unicode__(self):
        return unicode(self.qualification)

        # class Meta:
        #     verbose_name = '资质'
        #     verbose_name_plural = '资质'


class Author(models.Model):
    author = models.CharField('作者', max_length=50)
    title = models.CharField('标题', max_length=150)
    qualification = models.ForeignKey(Qualification)
    mark = models.ManyToManyField(Mark)
    blog = models.TextField('博客内容')
    time = models.DateField('写作日期')

    def __unicode__(self):
        return unicode(self.author,)

    class Meta:
        ordering = ['time']
        # verbose_name = '相关博客'
        # verbose_name_plural = '相关博客'


class Objectattribution(models.Model):
    attribution = models.CharField('归属', max_length=50)
    place = models.PositiveIntegerField('地点', default=0)

    def __unicode__(self):
        return unicode(self.attribution)


class Myobject(models.Model):
    object = models.CharField('物品', max_length=50)
    content = models.CharField('产品内容',max_length=255)
    attribution=models.ForeignKey(Objectattribution)
    order=models.PositiveIntegerField('顺序',default=0)
    bontime = models.DateField('生产日期')

    def __unicode__(self):
        return unicode(self.object)

        # class Meta:
        #     verbose_name = '物品'
        #     verbose_name_plural = '物品'


class Adress(models.Model):
    receivename = models.CharField('收件姓名', max_length=50)
    adress = models.TextField('收件地址')

    def __unicode__(self):
        return unicode(self.receivename)

        # class Meta:
        #     verbose_name = '收件地址'
        #     verbose_name_plural = '收件地址'


class CustomView(models.Model):
    pass
