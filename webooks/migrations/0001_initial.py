# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'webooks_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'webooks', ['Book'])

        # Adding model 'Chapter'
        db.create_table(u'webooks_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['webooks.Book'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=1048576)),
        ))
        db.send_create_signal(u'webooks', ['Chapter'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'webooks_book')

        # Deleting model 'Chapter'
        db.delete_table(u'webooks_chapter')


    models = {
        u'webooks.book': {
            'Meta': {'object_name': 'Book'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'webooks.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webooks.Book']"}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1048576'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['webooks']