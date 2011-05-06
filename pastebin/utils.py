import pygments
from pygments.util import ClassNotFound
from pygments.lexers import get_lexer_by_name, get_lexer_for_filename, get_lexer_for_mimetype, PhpLexer, TextLexer

from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter

LANGUAGES = {
    'text':             'Text',
    #'multi':           'Multi-File',
    'python':           'Python',
    'pycon':            'Python Console Sessions',
    'pytb':             'Python Tracebacks',
    'html+php':         'PHP',
    #'php':             'PHP (inline)',
    'html+django':      'Django / Jinja Templates',
    'html+mako':        'Mako Templates',
    'html+myghty':      'Myghty Templates',
    'apache':           'Apache Config (.htaccess)',
    'bash':             'Bash',
    'bat':              'Batch (.bat)',
    'brainfuck':        'Brainfuck',
    'c':                'C',
    #'gcc-messages':    'GCC Messages',
    'cpp':              'C++',
    'csharp':           'C#',
    'css':              'CSS',
    #'csv':             'CSV',
    'd':                'D',
    'minid':            'MiniD',
    'smarty':           'Smarty',
    'glsl':             'GL Shader language',
    'html':             'HTML',
    'html+genshi':      'Genshi Templates',
    'js':               'JavaScript',
    'java':             'Java',
    #'javac-messages':  'javac Messages',
    'jsp':              'JSP',
    'lua':              'Lua',
    'haskell':          'Haskell',
    'literate-haskell': 'Literate Haskell',
    'scheme':           'Scheme',
    'ruby':             'Ruby',
    'irb':              'Interactive Ruby',
    'ini':              'INI File',
    'perl':             'Perl',
    'rhtml':            'eRuby / rhtml',
    'tex':              'TeX / LaTeX',
    'xml':              'XML',
    'rst':              'reStructuredText',
    'irc':              'IRC Logs',
    #'diff':            'Unified Diff',
    'vim':              'Vim Scripts',
    'ocaml':            'OCaml',
    'sql':              'SQL',
    'mysql':            'MySQL',
    'squidconf':        'SquidConf',
    'sourceslist':      'sources.list',
    'erlang':           'Erlang',
    'vim':              'Vim',
    'dylan':            'Dylan',
    'gas':              'GAS',
    'nasm':             'Nasm',
    'llvm':             'LLVM',
    #'creole':          'Creole Wiki',
    'clojure':          'Clojure',
    'io':               'IO',
    'objectpascal':     'Object-Pascal',
    'scala':            'Scala',
    'boo':              'Boo',
    'matlab':           'Matlab',
    'matlabsession':    'Matlab Session',
    'povray':           'Povray',
    'smalltalk':        'Smalltalk',
    'control':          'Debian control-files',
    'gettext':          'Gettext catalogs',
    'lighttpd':         'Lighttpd',
    'nginx':            'Nginx',
    'yaml':             'YAML',
    'xslt':             'XSLT',
    'go':               'Go',
}

def get_language(code):
    return LANGUAGES.get(code, 'Undefined language')

def highlight(code, language):
    try:
        lexer = get_lexer_by_name(language)
    except ClassNotFound:
        lexer = TextLexer()
    style = "monokai"
    formatter = HtmlFormatter(linenos=True, cssclass="syntax", style=style)
    return u'<div class="highlight">%s</div>' % pygments.highlight(code, lexer, formatter)
