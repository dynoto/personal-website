# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.star'
        db.add_column('photographs_image', 'star',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.star'
        db.delete_column('photographs_image', 'star')


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
            'star': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'uploaded': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['photographs']