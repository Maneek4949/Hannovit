# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
import json

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        with open('blog_details.json', encoding="utf8") as f:
            blogs = json.load(f)
        return blogs

    def location(self, item):
        return reverse('blog_detail', args=[item['id']])

class IndustriesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        with open('industries.json', encoding="utf8") as f:
            industries = json.load(f)
        return industries

    def location(self, item):
        return reverse('industries_detail', args=[item['id']])

class PortfolioSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        with open('portfolio.json', encoding="utf8") as f:
            portfolio = json.load(f)
        return portfolio

    def location(self, item):
        return reverse('portfolio_detail', args=[item['id']])
