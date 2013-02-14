# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field technologies on 'Project'
        db.create_table('portfolios_project_technologies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['portfolios.project'], null=False)),
            ('technology', models.ForeignKey(orm['portfolios.technology'], null=False))
        ))
        db.create_unique('portfolios_project_technologies', ['project_id', 'technology_id'])

        # Removing M2M table for field projects on 'Technology'
        db.delete_table('portfolios_technology_projects')


    def backwards(self, orm):
        # Removing M2M table for field technologies on 'Project'
        db.delete_table('portfolios_project_technologies')

        # Adding M2M table for field projects on 'Technology'
        db.create_table('portfolios_technology_projects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('technology', models.ForeignKey(orm['portfolios.technology'], null=False)),
            ('project', models.ForeignKey(orm['portfolios.project'], null=False))
        ))
        db.create_unique('portfolios_technology_projects', ['technology_id', 'project_id'])


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolios.Technology']", 'symmetrical': 'False'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'portfolios.technology': {
            'Meta': {'object_name': 'Technology'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['portfolios']