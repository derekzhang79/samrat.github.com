from pelican.plugins import related_posts

SITEURL = 'http://samrat.me'
ABOUT = '18 year-old from Nepal interested in computers and technology'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

#META
META_DESCRIPTION = "Personal website and blog of Samrat Man Singh. Follow him at @samratmansing"
META_KEYWORDS = "Samrat Man Singh, python, flask, computers, technology, nepal"

PLUGINS = [related_posts]

AUTHOR = 'Samrat Man Singh'

RELATIVE_URLS = False

#DEFAULT_CATEGORY = ''
OUTPUT_PATH = './'

DEFAULT_PAGINATION = 5
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = True

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SITENAME = 'Samrat Man Singh'
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.xml'
FEED_ATOM = 'feeds/atom.xml'
FEED_URL = 'http://feeds.feedburner.com/SamratDotMe'


TWITTER_USERNAME = 'samratmansingh'
GOOGLE_ANALYTICS = 'UA-18986645-3'
DISQUS_SITENAME = 'samratmansingh'

SOCIAL = (('Projects', '/projects'),
    ('Twitter', 'http://twitter.com/samratmansingh'),
          ('Github', 'http://github.com/samrat'),
          ('Contact', 'mailto:samrat@samrat.me'),)

ARTICLE_FOOTER = "If you liked this post, you should <a href='http://twitter.com/samratmansingh'>follow me on Twitter.</a>"

TIMEZONE = "Asia/Kathmandu"

THEME = '/home/samrat/code/syte-pelican'
MEDIA_URL = 'theme/'
TWITTER_INTEGRATION_ENABLED = True
GITHUB_INTEGRATION_ENABLED = True
DRIBBBLE_INTEGRATION_ENABLED = False
INSTAGRAM_INTEGRATION_ENABLED = True
DISQUS_INTEGRATION_ENABLED = False
