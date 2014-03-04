# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mark'
        db.create_table(u'blog_mark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mark', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'blog', ['Mark'])

        # Adding model 'Qualification'
        db.create_table(u'blog_qualification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'blog', ['Qualification'])

        # Adding model 'Author'
        db.create_table(u'blog_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('qualification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Qualification'])),
            ('blog', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'blog', ['Author'])

        # Adding M2M table for field mark on 'Author'
        m2m_table_name = db.shorten_name(u'blog_author_mark')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(orm[u'blog.author'], null=False)),
            ('mark', models.ForeignKey(orm[u'blog.mark'], null=False))
        ))
        db.create_unique(m2m_table_name, ['author_id', 'mark_id'])

        # Adding model 'Myobject'
        db.create_table(u'blog_myobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('bontime', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'blog', ['Myobject'])

        # Adding model 'Adress'
        db.create_table(u'blog_adress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('receivename', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('adress', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['Adress'])

        # Adding model 'CustomView'
        db.create_table(u'blog_customview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'blog', ['CustomView'])


    def backwards(self, orm):
        # Deleting model 'Mark'
        db.delete_table(u'blog_mark')

        # Deleting model 'Qualification'
        db.delete_table(u'blog_qualification')

        # Deleting model 'Author'
        db.delete_table(u'blog_author')

        # Removing M2M table for field mark on 'Author'
        db.delete_table(db.shorten_name(u'blog_author_mark'))

        # Deleting model 'Myobject'
        db.delete_table(u'blog_myobject')

        # Deleting model 'Adress'
        db.delete_table(u'blog_adress')

        # Deleting model 'CustomView'
        db.delete_table(u'blog_customview')


    models = {
        u'blog.adress': {
            'Meta': {'object_name': 'Adress'},
            'adress': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receivename': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.author': {
            'Meta': {'object_name': 'Author'},
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['blog']