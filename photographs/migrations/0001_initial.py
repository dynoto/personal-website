# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('photographs_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('photographs', ['Category'])

        # Adding model 'Image'
        db.create_table('photographs_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photographs.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('likes', self.gf('django.db.models.fields.IntegerField')()),
            ('uploaded', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('photographs', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('photographs_category')

        # Deleting model 'Image'
        db.delete_table('photographs_image')


    models = {
        'photographs.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'photographs.image': {
            'Meta': {'object_name': 'Image'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photographs.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uploaded': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['photographs']