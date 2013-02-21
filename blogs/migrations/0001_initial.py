# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('blogs_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 18, 0, 0), blank=True)),
        ))
        db.send_create_signal('blogs', ['Tag'])

        # Adding model 'Article'
        db.create_table('blogs_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 18, 0, 0), blank=True)),
            ('script', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('stylesheet', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('like', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('blogs', ['Article'])

        # Adding M2M table for field tags on 'Article'
        db.create_table('blogs_article_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['blogs.article'], null=False)),
            ('tag', models.ForeignKey(orm['blogs.tag'], null=False))
        ))
        db.create_unique('blogs_article_tags', ['article_id', 'tag_id'])

        # Adding model 'Comment'
        db.create_table('blogs_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 18, 0, 0), blank=True)),
        ))
        db.send_create_signal('blogs', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('blogs_tag')

        # Deleting model 'Article'
        db.delete_table('blogs_article')

        # Removing M2M table for field tags on 'Article'
        db.delete_table('blogs_article_tags')

        # Deleting model 'Comment'
        db.delete_table('blogs_comment')


    models = {
        'blogs.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 18, 0, 0)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'script': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'stylesheet': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blogs.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'blogs.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 18, 0, 0)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'blogs.tag': {
            'Meta': {'object_name': 'Tag'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 18, 0, 0)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blogs']