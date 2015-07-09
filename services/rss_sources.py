bbcRss = {}
bbcRss['top-stories'] = 'http://feeds.bbci.co.uk/news/rss.xml'
bbcRss['world'] = 'http://feeds.bbci.co.uk/news/world/rss.xml'
bbcRss['uk'] = 'http://feeds.bbci.co.uk/news/uk/rss.xml'
bbcRss['business'] = 'http://feeds.bbci.co.uk/news/business/rss.xml'
bbcRss['politics'] = 'http://feeds.bbci.co.uk/news/politics/rss.xml'
bbcRss['health'] = 'http://feeds.bbci.co.uk/news/health/rss.xml'
bbcRss['education-and-family'] = 'http://feeds.bbci.co.uk/news/education/rss.xml'
bbcRss['science-and-environment'] = 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml'
bbcRss['technology'] = 'http://feeds.bbci.co.uk/news/technology/rss.xml'
bbcRss['entertainment-and-arts'] = 'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml'

cbcRss = {}
cbcRss['top-stories'] = 'http://rss.cbc.ca/lineup/topstories.xml'
cbcRss['world'] = 'http://rss.cbc.ca/lineup/world.xml'
cbcRss['canada'] = 'http://rss.cbc.ca/lineup/canada.xml'
cbcRss['business'] = 'http://rss.cbc.ca/lineup/business.xml'
cbcRss['politics'] = 'http://rss.cbc.ca/lineup/politics.xml'
cbcRss['health'] = 'http://rss.cbc.ca/lineup/health.xml'
cbcRss['technology-and-science'] = 'http://rss.cbc.ca/lineup/technology.xml'
cbcRss['sports'] = 'http://rss.cbc.ca/lineup/sports.xml'
cbcRss['toronto'] = 'http://rss.cbc.ca/lineup/canada-toronto.xml'
cbcRss['arts-and-entertainment'] = 'http://rss.cbc.ca/lineup/arts.xml'

reutersRss = {}
reutersRss['top-stories'] = 'http://feeds.reuters.com/reuters/topNews'
reutersRss['world'] = 'http://feeds.reuters.com/Reuters/worldNews'
reutersRss['us'] = 'http://feeds.reuters.com/Reuters/domesticNews'
reutersRss['business'] = 'http://feeds.reuters.com/reuters/businessNews'
reutersRss['politics'] = 'http://feeds.reuters.com/Reuters/PoliticsNews'
reutersRss['science'] = 'http://feeds.reuters.com/reuters/technologyNews'
reutersRss['health'] = 'http://feeds.reuters.com/reuters/healthNews'
reutersRss['technology'] = 'http://feeds.reuters.com/reuters/technologyNews'
reutersRss['sports'] = 'http://feeds.reuters.com/reuters/sportsNews'
reutersRss['entertainment'] = 'http://feeds.reuters.com/reuters/entertainment'

def getBbcRss():
	return bbcRss

def getCbcRss():
	return cbcRss

def getReutersRss():
	return reutersRss
