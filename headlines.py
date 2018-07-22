import feedparser
from flask import Flask, render_template


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
'cnn': 'http://rss.cnn.com/rss/edition.rss.xml',
'fox': 'http://feeds.foxnews.com/foxnews/latest.xml'
}


def get_news(publication):
    ''' Get news title, pulication date, summary for the first article of rss feed of publication '''
    rss = feedparser.parse(RSS_FEEDS[publication])
    first_article = rss.entries[0]
    news_title = first_article.get("title")
    pub_date = first_article.get("published")
    summary = first_article.get("description")
    return render_template("Index.html", publication = publication.upper(), news_title = news_title, pub_date = pub_date, summary = summary)

@app.route("/")
@app.route("/bbc")
def def_bbc_news():
    ''' Default Page : Gives listing of first headline in bbc '''
    return get_news('bbc')
	
	
@app.route("/cnn")
def def__cnn_news():
    ''' Default Page : Gives listing of first headline in cnn'''
    return get_news('cnn')
	
	
if __name__ == '__main__':
    app.run(port = 5000, debug = True)