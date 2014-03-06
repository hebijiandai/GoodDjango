# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table(u'blog_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Autoignition_temperature', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Binary_phase_diagram', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Boiling_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Coefficient_of_thermal_expansion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Critical_temperature', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Curie_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Emissivity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Eutectic_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Flammability', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Flash_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Glass_transition_temperature', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Heat_of_fusion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Heat_of_vaporization', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Inversion_temperature', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Melting_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Phase_diagram', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Pyrophoricity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Solidus', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Specific_heat', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Thermal_conductivity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Thermal_diffusivity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Thermal_expansion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Seebeck_coefficient', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Triple_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Vapor_pressure', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('Vicat_softening_point', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'blog', ['Material'])

        # Adding field 'Myobject.material'
        db.add_column(u'blog_myobject', 'material',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['blog.Material']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table(u'blog_material')

        # Deleting field 'Myobject.material'
        db.delete_column(u'blog_myobject', 'material_id')


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
        u'blog.material': {
            'Autoignition_temperature': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Binary_phase_diagram': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Boiling_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Coefficient_of_thermal_expansion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Critical_temperature': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Curie_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Emissivity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Eutectic_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Flammability': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Flash_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Glass_transition_temperature': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Heat_of_fusion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Heat_of_vaporization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Inversion_temperature': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Melting_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Meta': {'object_name': 'Material'},
            'Phase_diagram': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Pyrophoricity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Seebeck_coefficient': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Solidus': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Specific_heat': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Thermal_conductivity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Thermal_diffusivity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Thermal_expansion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Triple_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Vapor_pressure': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'Vicat_softening_point': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.myobject': {
            'Meta': {'object_name': 'Myobject'},
            'attribution': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Objectattribution']"}),
            'bontime': ('django.db.models.fields.DateField', [], {}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Material']"}),
            'object': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'blog.objectattribution': {
            'Meta': {'object_name': 'Objectattribution'},
            'attribution': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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