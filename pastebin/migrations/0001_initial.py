# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Snippet'
        db.create_table('pastebin_snippet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('code_highlight', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lexer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('expires_options', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('expires_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=255, blank=True)),
        ))
        db.send_create_signal('pastebin', ['Snippet'])


    def backwards(self, orm):
        
        # Deleting model 'Snippet'
        db.delete_table('pastebin_snippet')


    models = {
        'pastebin.snippet': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Snippet'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'code_highlight': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expires_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'expires_options': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lexer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['pastebin']
