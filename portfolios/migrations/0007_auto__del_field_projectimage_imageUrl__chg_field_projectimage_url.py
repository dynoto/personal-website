# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProjectImage.imageUrl'
        db.delete_column('portfolios_projectimage', 'imageUrl')


        # Changing field 'ProjectImage.url'
        db.alter_column('portfolios_projectimage', 'url', self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding field 'ProjectImage.imageUrl'
        db.add_column('portfolios_projectimage', 'imageUrl',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=200, null=True),
                      keep_default=False)


        # Changing field 'ProjectImage.url'
        db.alter_column('portfolios_projectimage', 'url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        'portfolios.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolios.Technology']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portfolios.projectimage': {
            'Meta': {'object_name': 'ProjectImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projectImages'", 'to': "orm['portfolios.Project']"}),
            'url': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'null': 'True'})
        },
        'portfolios.technology': {
            'Meta': {'object_name': 'Technology'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['portfolios']