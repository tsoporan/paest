from django.db import models

from pygments.lexers import get_all_lexers, get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
from pygments.lexers import ClassNotFound
from django.utils import timezone
from random import choice
import string

from pastebin.utils import LANGUAGES, highlight

LEXERS = tuple(sorted(((k,v) for k,v in LANGUAGES.items())))

EXPIRE_OPTIONS = (
    (60, 'One Minute'), 
    (3600, 'One Hour'), 
    (3600*24*7, 'One Week'), 
    (3600*24*30, 'One Month'), 
)

def gen_url(length=4, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

class Snippet(models.Model):
    created = models.DateTimeField('Created',auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)
    code = models.TextField('Codez', help_text="This is where you put your obfuscated code. :P")
    code_highlight = models.TextField('Highlighted Code', blank=True, editable=False)
    lexer = models.CharField('Language', max_length=255, choices=LEXERS, default="python", blank=True, null=True, help_text="Specify a language. We'll try to guess it otherwise. (This works best with a shebang.)")
    expires_options = models.IntegerField('Expires', choices=EXPIRE_OPTIONS, blank=True, null=True, help_text="When to expire =(")
    expires_date = models.DateTimeField('Expires Date', blank=True, null=True)
    url = models.SlugField('URL', max_length=255, blank=True)
    locked = models.BooleanField("Lock", default=0, help_text="Lock so it can't be edited.")

    class Meta:
        ordering = ('-created',)

    def is_expired(self):
        if self.expires_date:
            return timezone.now() > self.expires_date
        return False

    def line_count(self):
        return len(self.code.splitlines())

    def line_split(self):
        return self.code_highlight.splitlines()

    def save(self, *args, **kwargs):
        if not self.lexer:
            lexer = guess_lexer(self.code)
            lexer = lexer.name.lower()
            self.lexer = lexer

        self.code_highlight = highlight(self.code, self.lexer)

        if self.expires_options:
            self.expires_date = timezone.now() + timezone.timedelta(seconds=int(self.expires_options))

        #if no url is supplied, created a random unique one
        if not self.url:
            self.url = gen_url()
        super(Snippet, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.url

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {'url': self.url})

