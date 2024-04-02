from django.urls import path
from django.views.generic import TemplateView

from .views import  news_detail, HomePageView, \
 ContactPageView, LocalNewsView, SubjectNewsView, SportNewsView, \
    WorldNewsView, IqtisodiyotNewsView


urlpatterns = [
    # path('uzbekistan/', UzbekistanPageView, name="uzbekistan"),
    # path('Jahon/', JahonPageView, name="Jahon"),
    # path('Fan-texnika/', Fan_texnikaPageView, name="Fan-texnika"),
    # path('Sport/', SportPageView, name="Sport"),
    # path('single/', SinglePageView, name="single"),
    # path('news/', news_list, name="news_all"),
    path('news/<slug:news>/', news_detail, name="news_detail_page"),

    path('', HomePageView.as_view(), name="homepage"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('about/', TemplateView.as_view(template_name="news/about.html"), name="about-us"),
    path('local/', LocalNewsView.as_view(template_name="news/local.html"), name="local-news"),
    path('world/', WorldNewsView.as_view(template_name="news/World.html"), name="world-news"),
    path('fan/', SubjectNewsView.as_view(template_name="news/Fan-texnika.html"), name="fan-news"),
    path('sport/', SportNewsView.as_view(template_name="news/Sport.html"), name="sport-news"),
    path('iqtisodiyot/', IqtisodiyotNewsView.as_view(template_name="news/Iqtisodiyot.html"), name="iqtisodiyot-news"),

]
