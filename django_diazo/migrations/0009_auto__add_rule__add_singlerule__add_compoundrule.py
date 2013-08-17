# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rule'
        db.create_table(u'django_diazo_rule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_diazo', ['Rule'])

        # Adding model 'SingleRule'
        db.create_table(u'django_diazo_singlerule', (
            (u'rule_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['django_diazo.Rule'], unique=True, primary_key=True)),
            ('rule', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'django_diazo', ['SingleRule'])

        # Adding model 'CompoundRule'
        db.create_table(u'django_diazo_compoundrule', (
            (u'rule_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['django_diazo.Rule'], unique=True, primary_key=True)),
            ('prefix', self.gf('django.db.models.fields.TextField')()),
            ('suffix', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'django_diazo', ['CompoundRule'])

        # Adding M2M table for field rules on 'CompoundRule'
        m2m_table_name = db.shorten_name(u'django_diazo_compoundrule_rules')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compoundrule', models.ForeignKey(orm[u'django_diazo.compoundrule'], null=False)),
            ('rule', models.ForeignKey(orm[u'django_diazo.rule'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compoundrule_id', 'rule_id'])


    def backwards(self, orm):
        # Deleting model 'Rule'
        db.delete_table(u'django_diazo_rule')

        # Deleting model 'SingleRule'
        db.delete_table(u'django_diazo_singlerule')

        # Deleting model 'CompoundRule'
        db.delete_table(u'django_diazo_compoundrule')

        # Removing M2M table for field rules on 'CompoundRule'
        db.delete_table(db.shorten_name(u'django_diazo_compoundrule_rules'))


    models = {
        u'django_diazo.compoundrule': {
            'Meta': {'object_name': 'CompoundRule', '_ormbases': [u'django_diazo.Rule']},
            'prefix': ('django.db.models.fields.TextField', [], {}),
            u'rule_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_diazo.Rule']", 'unique': 'True', 'primary_key': 'True'}),
            'rules': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'compound_rule'", 'symmetrical': 'False', 'to': u"orm['django_diazo.Rule']"}),
            'suffix': ('django.db.models.fields.TextField', [], {})
        },
        u'django_diazo.rule': {
            'Meta': {'object_name': 'Rule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_diazo.singlerule': {
            'Meta': {'object_name': 'SingleRule', '_ormbases': [u'django_diazo.Rule']},
            'rule': ('django.db.models.fields.TextField', [], {}),
            u'rule_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['django_diazo.Rule']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'django_diazo.theme': {
            'Meta': {'object_name': 'Theme'},
            'builtin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'debug': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_diazo']