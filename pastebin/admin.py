from django.contrib import admin
from paest.pastebin.models import Snippet
import datetime

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'code_head', 'url', 'created', 'has_expired')

    def has_expired(self, obj):
        if obj.expires_date:
            return datetime.datetime.now() > obj.expires_date
        else: return False
    
    def code_head(self, obj):
        return obj.code[:40] + ' ...'

admin.site.register(Snippet, SnippetAdmin)
