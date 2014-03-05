# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Qualification.charactor'
        db.add_column(u'blog_qualification', 'charactor',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=50),
                      keep_default=False)

        # Adding field 'Qualification.level'
        db.add_column(u'blog_qualification', 'level',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Qualification.charactor'
        db.delete_column(u'blog_qualification', 'charactor')

        # Deleting field 'Qualification.level'
        db.delete_column(u'blog_qualification', 'level')


    models = {
        u'blog.adress': {
            'Meta': {'object_name': 'Adress'},
            'adress': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receivename': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.author': {
            'Meta': {'ordering': "['time']", 'object_name': 'Author'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'blog': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Mark']", 'symmetrical': 'False'}),
            'qualification': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Qualification']"}),
            'time': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'blog.customview': {
            'Meta': {'object_name': 'CustomView'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'blog.mark': {
            'Meta': {'object_name': 'Mark'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mark': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.myobject': {
            'Meta': {'object_name': 'Myobject'},
            'bontime': ('django.db.models.fields.DateField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.qualification': {
            'Meta': {'object_name': 'Qualification'},
            'charactor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.SmallIntegerField', [], {}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']