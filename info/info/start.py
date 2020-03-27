from scrapy import cmdline

name = 'base -s LOG_FILE=all.log'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
