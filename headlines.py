import feedparser
from flask import Flask, render_template


app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def def_news():
    ''' Default Page : Gives listing of all headlines '''
    feed = feedparser.parse(BBC_FEED)
    #first_article = feed.entries[0]
    #news_title = first_article.get("title")
    #pub_date = first_article.get("pubDate")
    #summary = first_article.get("description")
    return str(feed)
    #eturn render_template("Index.html", news_title = news_title, pub_date = pub_date, summary = summary)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)