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


class MarkAdmin(admin.ModelAdmin):
    list_display = ('mark',)


admin.site.register(Mark, MarkAdmin)


class QualificationAdmin(admin.ModelAdmin):
    list_display = ('qualification',)


admin.site.register(Qualification, QualificationAdmin)


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
        # 排除多对多字段
        # exclued=('mark',)

class MarkChoices(AutoModelSelect2MultipleField):
    queryset = Mark.objects
    search_fields = ['name_icontains']

class QualificationChoices(AutoModelSelect2Field):
    queryset = Qualification.objects
    search_fields=['name_icontains']


class AuthorForm(ModelForm):
    mark = MarkChoices(
        label='博客标签',
    )

    qualification = QualificationChoices(
        label='资质',
        widget=AutoHeavySelect2Widget(
            select2_options={
                'width': '30px',
                'placeholder': 'Lookup ...'
            }
        )
    )
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
            'title': EnclosedInput(prepend='icon-globe', append='end with',
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


class MyobjectForm(ModelForm):
    class Meta:
        model = Myobject

        widgets = {
            'content': RedactorWidget,
            # 下面的富文本框有点难度，显示不完美
            # 'content': CKEditorWidget(editor_options={'startupFocus': False}),
        }


class MyobjectAdmin(admin.ModelAdmin):
    form = MyobjectForm
    search_fields = ('object', 'content')
    list_display = ('object', 'bontime',)


admin.site.register(Myobject, MyobjectAdmin)


class AdressAdmin(admin.ModelAdmin):
    list_display = ('receivename', 'adress')


admin.site.register(Adress, AdressAdmin)
