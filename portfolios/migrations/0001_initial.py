# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('portfolios_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('portfolios', ['Project'])

        # Adding model 'Image'
        db.create_table('portfolios_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolios.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('portfolios', ['Image'])

        # Adding model 'Technology'
        db.create_table('portfolios_technology', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('portfolios', ['Technology'])

        # Adding M2M table for field projects on 'Technology'
        db.create_table('portfolios_technology_projects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('technology', models.ForeignKey(orm['portfolios.technology'], null=False)),
            ('project', models.ForeignKey(orm['portfolios.project'], null=False))
        ))
        db.create_unique('portfolios_technology_projects', ['technology_id', 'project_id'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('portfolios_project')

        # Deleting model 'Image'
        db.delete_table('portfolios_image')

        # Deleting model 'Technology'
        db.delete_table('portfolios_technology')

        # Removing M2M table for field projects on 'Technology'
        db.delete_table('portfolios_technology_projects')


    models = {
        'portfolios.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolios.Project']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'portfolios.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolios.technology': {
            'Meta': {'object_name': 'Technology'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolios.Project']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['portfolios']