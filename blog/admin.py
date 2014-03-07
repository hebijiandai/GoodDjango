# coding:utf-8
from django.contrib import admin
from blog.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from django.forms import ModelForm
# from suit_ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget
from django_select2 import *
from suit.widgets import *
from suit.admin import *
from reversion import VersionAdmin


class MarkAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('mark', 'license')


admin.site.register(Mark, MarkAdmin)


class QualificationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('qualification', 'license', 'charactor', 'level')


admin.site.register(Qualification, QualificationAdmin)


class AuthorResource(resources.ModelResource):

    class Meta:
        model = Author

class AuthorForm(ModelForm):
    mark = ModelSelect2MultipleField(
        label="博客标签", queryset=Mark.objects, required=False)
    qualification = ModelSelect2Field(
        label="个人资质", queryset=Qualification.objects, required=False)
    # 有一个地方没解决：要设置自动下拉框
    # qualification = QualificationChoices(
    #     label='资质',
    #     widget=AutoHeavySelect2Widget(
    #         select2_options={
    #             'width': '30px',
    #             'placeholder': 'Lookup ...'
    #         }
    #     )
    # )

    class Meta:
        model = Author
        widgets = {
            'blog': RedactorWidget,
            # 'blog':  CKEditorWidget,
            'author': EnclosedInput(prepend='icon-user',
                                    append='<input type="button" '
                                           'class="btn" onclick="window'
                                           '.open(\'https://www.google'
                                           '.com/\')" value="Search">',
                                    attrs={'class': 'input-small'}),
            'title': EnclosedInput(prepend='icon-globe', append='Consult Sherock Holmels',
                                   attrs={'class': 'input-small'}),

        }


class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('author', 'title', 'mark', 'blog')
    list_display = ('author', 'title', 'time')

    resource_class = AuthorResource
    form = AuthorForm

    fieldsets = [

        (None,
         {'fields': ['author', 'mark', 'title', 'qualification', 'time']}),

        ('博客内容', {
            'classes': ('full-width',),
            'description': '请添加博客内容',
            'fields': ['blog']}),

    ]


admin.site.register(Author, AuthorAdmin)
# 主从表格式从这行开始,外键的做附属，被外键的做主表


class MyobjectInlineForm(ModelForm):

    class Meta:
        widgets = {
            'object': TextInput(attrs={'class': 'input-small'}),
            'content': TextInput(attrs={'class': 'input-medium'}),
            # 'attribution': TextInput(attrs={'class': 'input-mini'}),不能加
            'material': Select(attrs={'class': 'input-small'}),
            'bontime': SuitDateWidget,

        }


class MyobjectInline(SortableTabularInline):
    form = MyobjectInlineForm
    model = Myobject
    fields = ('object', 'content', 'attribution', 'material', 'bontime')
    extra = 1
    verbose_name_plural = '物品列表子窗体'
    sortable = 'order'


class MyObjectAttributionAdmin(ImportExportModelAdmin, SortableModelAdmin, admin.ModelAdmin):
    form = MyobjectInlineForm
    search_fields = ('attribution',)
    list_display = ('attribution', 'place', 'mynumber')
    inlines = (MyobjectInline,)
    sortable = 'place'

    def mynumber(self, obj):
        return len(obj.myobject_set.all())

admin.site.register(Objectattribution, MyObjectAttributionAdmin)


class MaterialForm(ModelForm):

    class Meta:
        model = Material
        widgets = {
            # 'material':RedactorWidget,
            'Autoignition_temperature': EnclosedInput(prepend='icon-leaf', append=' <sup>o</sup>C',
            attrs={'class': 'input-small'}),
            'Critical_temperature': EnclosedInput(prepend='icon-globe', append=' <sup>o</sup>C',
            attrs={'class': 'input-small'}),
        }


class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = MaterialForm
    list_display = ('material',)
    list_select_related = True



    fieldsets = [

        ('material', {
            # 'classes': ('full-width',),
            'classes': ('suit-tab suit-tab-material',),
            'description': 'Please input the material',
            'fields': ['material', 'Autoignition_temperature', 'Binary_phase_diagram',
            'Boiling_point', 'Coefficient_of_thermal_expansion', 'Critical_temperature', ]}),

        ('Eutectic point', {
            'classes': ('suit-tab suit-tab-eutectic',),
            'description': 'Please input the Eutectic point',
            'fields': ['Eutectic_point', 'Curie_point', 'Emissivity', 'Flammability',
            'Flash_point', 'Glass_transition_temperature',
           'Heat_of_fusion', 'Heat_of_vaporization', 'Inversion_temperature', ]}),

        ('Pyrophoricity', {
            'classes': ('suit-tab suit-tab-Pyrophoricity',),
            'description': 'Please input the Pyrophoricity',
            'fields': ['Pyrophoricity', 'Melting_point', 'Phase_diagram', 'Solidus',
           'Specific_heat', 'Thermal_conductivity', 'Thermal_diffusivity', ]}),

        ('montain', {
            'classes': ('suit-tab suit-tab-montain',),
            'description': 'Please input the montain',
            'fields': ['Thermal_expansion', 'Seebeck_coefficient',
            'Triple_point', 'Vapor_pressure', 'Vicat_softening_point', ]}),
    ]

    suit_form_tabs = (('material', '材料'), ('eutectic', '共晶点'),
                    ('Pyrophoricity', '自燃点'), ('montain', '山顶'),
                    ('my_custom_view','我的自定义材料网站'))

    suit_form_includes = (
        ('omg.html', 'middle','my_custom_view'),
    )

admin.site.register(Material, MaterialAdmin)


class MyobjectForm(ModelForm):
    attribution = ModelSelect2Field(
        label='归属', queryset=Objectattribution.objects, required=False)

    class Meta:
        model = Myobject


class MyobjectAdmin(ImportExportModelAdmin):
    form = MyobjectForm
    search_fields = ('object', 'content')
    list_display = ('object', 'attribution', 'bontime',)


admin.site.register(Myobject, MyobjectAdmin)


class AdressAdmin(VersionAdmin):
    list_display = ('receivename', 'adress')


admin.site.register(Adress, AdressAdmin)
