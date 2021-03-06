# Scrapy settings for splash_project project
BOT_NAME = 'splash_project'

SPIDER_MODULES = ['splash_project.spiders']
NEWSPIDER_MODULE = 'splash_project.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True


SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'