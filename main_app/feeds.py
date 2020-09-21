from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Sighting
from django.urls import reverse

class LatestPostsFeed(Feed):
    title = "Underwater Times"
    link = "https://www.underwatertimes.com/rss/newswire20.xml"
    description = "Breaking News."

    def feed(self):
        return self

    def feed_title(self, title):
        return self.title

    def feed_description(self, description):
        return truncatewords(self.description, 30)