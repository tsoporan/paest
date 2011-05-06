from django.contrib import admin
from paest.pastebin.models import Snippet
import datetime

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'created', 'has_expired')

    def has_expired(self, obj):
        if obj.expires_date:
            return datetime.datetime.now() > obj.expires_date
        else: return False

admin.site.register(Snippet, SnippetAdmin)
