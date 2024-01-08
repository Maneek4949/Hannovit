from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap, IndustriesSitemap, PortfolioSitemap

sitemaps = {
    'blog': BlogSitemap,
    'industries': IndustriesSitemap,
    'portfolio': PortfolioSitemap,
}

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('about/', views.About.as_view(),name='about'),
    path('service/', views.Service.as_view(),name='service'),
    path('service/<str:id>/',views.SerivceDetail.as_view(),name='service_detail'),
    path('blog/',views.BlogList.as_view(),name='blog_list'),
    path('blog/<str:id>/',views.BlogDetail.as_view(),name='blog_detail'),
    path('portfolio/',views.Portfolio.as_view(),name='portfolio'),
    path('portfolio/<str:id>/',views.PortfolioDetail.as_view(),name='portfolio_detail'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('privacy/',views.Privacy.as_view(),name='privacy'),
    path('term-and-condition/',views.Term.as_view(),name='term'),
    path('team/',views.Team.as_view(),name='team'),
    path('industries/',views.Industries.as_view(),name='industries'),
    path('industries/<str:id>/',views.IndustriesDetail.as_view(),name='industries_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]