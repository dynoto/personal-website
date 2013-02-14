# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('photographs_image')

        # Adding model 'PhotographImage'
        db.create_table('photographs_photographimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photographImages', to=orm['photographs.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image_s', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image_m', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 10, 0, 0), blank=True)),
            ('star', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('photographs', ['PhotographImage'])


    def backwards(self, orm):
        # Adding model 'Image'
        db.create_table('photographs_image', (
            ('uploaded', self.gf('django.db.models.fields.DateTimeField')()),
            ('star', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photographs.Category'])),
            ('image_s', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_m', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('image_l', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
        ))
        db.send_create_signal('photographs', ['Image'])

        # Deleting model 'PhotographImage'
        db.delete_table('photographs_photographimage')


    models = {
        'photographs.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'photographs.photographimage': {
            'Meta': {'object_name': 'PhotographImage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photographImages'", 'to': "orm['photographs.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_m': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_s': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'star': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 10, 0, 0)', 'blank': 'True'})
        }
    }

    complete_apps = ['photographs']