# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.filename'
        db.delete_column('photographs_image', 'filename')

        # Adding field 'Image.image_s'
        db.add_column('photographs_image', 'image_s',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Image.image_m'
        db.add_column('photographs_image', 'image_m',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Adding field 'Image.image_l'
        db.add_column('photographs_image', 'image_l',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Image.filename'
        db.add_column('photographs_image', 'filename',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Deleting field 'Image.image_s'
        db.delete_column('photographs_image', 'image_s')

        # Deleting field 'Image.image_m'
        db.delete_column('photographs_image', 'image_m')

        # Deleting field 'Image.image_l'
        db.delete_column('photographs_image', 'image_l')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_l': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'image_m': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'image_s': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'star': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['photographs']