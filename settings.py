ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'

AUTHOR = 'Samrat Man Singh'

#DEFAULT_CATEGORY = ''
OUTPUT_PATH = './'

DEFAULT_PAGINATION = 5
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = True

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SITENAME = 'Samrat Man Singh'
FEED_DOMAIN = 'http://samrat.me'
FEED_RSS = 'feeds/all.xml'

TWITTER_USERNAME = 'samratmansingh'
GOOGLE_ANALYTICS = 'UA-18986645-3'
DISQUS_SITENAME = 'samratmansingh'

SOCIAL = (('twitter', 'http://twitter.com/samratmansingh'),
          ('github', 'http://github.com/samrat'),)

TIMEZONE = "Asia/Kathmandu"

THEME = '/home/samrat/code/syte-pelican'
MEDIA_URL = 'theme/'
TWITTER_INTEGRATION_ENABLED = True
GITHUB_INTEGRATION_ENABLED = True
DRIBBBLE_INTEGRATION_ENABLED = False
INSTAGRAM_INTEGRATION_ENABLED = True
DISQUS_INTEGRATION_ENABLED = False
