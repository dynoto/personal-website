# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('portfolios_image')

        # Adding model 'ProjectImage'
        db.create_table('portfolios_projectimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projectImages', to=orm['portfolios.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(default='-', max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('portfolios', ['ProjectImage'])


    def backwards(self, orm):
        # Adding model 'Image'
        db.create_table('portfolios_image', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolios.Project'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('portfolios', ['Image'])

        # Deleting model 'ProjectImage'
        db.delete_table('portfolios_projectimage')


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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'portfolios.technology': {
            'Meta': {'object_name': 'Technology'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['portfolios']