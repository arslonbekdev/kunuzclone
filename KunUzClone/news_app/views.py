from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import TemplateView , ListView

from news_app.forms import ContactForm
from news_app.models import News, Category


# Create your views here.

# def news_list(request):
#
#     news_list = News.objects.filter(status=News.Status.Published)
#     context = {
#         "news_list": news_list
#     }
#     return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)



# def HomePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:3]
#     local_1 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[1]
#     local_2 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[2]
#     local_3 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[3]
#     local_4 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[4]
#     worlds = News.published.all().filter(category__name="World").order_by('-publish_time')
#
#
#     context = {
#         "categories": categories,
#         "news_list": news_list,
#         "local_1": local_1,
#         "local_2": local_2,
#         "local_3": local_3,
#         "local_4": local_4,
#         "worlds": worlds
#     }
#
#     return render(request, "news/home.html", context)


class HomePageView(TemplateView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')
        context['local_news'] = News.published.all().filter(category__name='Uzbekistan')[:6]
        context['world_news'] = News.published.all().filter(category__name='World')[0:4]
        context['sport_news'] = News.published.all().filter(category__name='Sport').order_by("-publish_time")[:6]
        context['techno_news'] = News.published.all().filter(category__name='FAn-texnika').order_by("-publish_time")[:6]
        context['economy'] = News.published.all().filter(category__name='Iqtisodiyot').order_by("-publish_time")[:6]
        context['galery'] = News.published.all().filter(category__name='Iqtisodiyot').order_by("-publish_time")[0:6]

        return context


# def UzbekistanPageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:3]
#     local_1 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[0]
#     local_2 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[1]
#     local_3 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[2]
#     local_4 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[3]
#     local_5 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[4]
#     local_6 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[5]
#     local_7 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[6]
#     local_8 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[7]
#     local_9 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[8]
#     local_10 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[9]
#     local_11 = News.published.all().filter(category__name="Uzbekistan").order_by('-publish_time')[10]
#
#
#
#
#     context = {
#         "categories": categories,
#         "news_list": news_list,
#         "local_1": local_1,
#         "local_2": local_2,
#         "local_3": local_3,
#         "local_4": local_4,
#         "local_5": local_5,
#         "local_6": local_6,
#         "local_7": local_7,
#         "local_8": local_8,
#         "local_9": local_9,
#         "local_10": local_10,
#         "local_11": local_11,
#
#     }
#
#     return render(request, 'news/local.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'localnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Uzbekistan")
        return news


class WorldNewsView(ListView):
    model = News
    template_name = 'news/world.html'
    context_object_name = 'worldnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="World")[:3]
        return news



class ContactPageView(TemplateView):
    templates_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, "news/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Xabaringiz yuborildi </h2>")
        context = {
            "form": form
        }

        return render(request, "news/contact.html", context)


# def SinglePageView(request):
#
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:3]
#
#     context = {
#         "categories": categories,
#         "news_list": news_list,
#     }
#
#     return render(request, 'news/Iqtisodiyot.html', context)


class IqtisodiyotNewsView(ListView):
    model = News
    template_name = 'news/Iqtisodiyot.html'
    context_object_name = 'iqtisodnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Iqtisodiyot")
        return news


# def JahonPageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:3]
#     local_1 = News.published.all().filter(category__name="World").order_by('-publish_time')[0]
#     local_2 = News.published.all().filter(category__name="World").order_by('-publish_time')[1]
#     local_3 = News.published.all().filter(category__name="World").order_by('-publish_time')[2]
#     local_4 = News.published.all().filter(category__name="World").order_by('-publish_time')[3]
#     local_5 = News.published.all().filter(category__name="World").order_by('-publish_time')[4]
#     local_6 = News.published.all().filter(category__name="World").order_by('-publish_time')[5]
#     local_7 = News.published.all().filter(category__name="World").order_by('-publish_time')[6]
#     local_8 = News.published.all().filter(category__name="World").order_by('-publish_time')[7]
#     local_9 = News.published.all().filter(category__name="World").order_by('-publish_time')[8]
#     local_10 = News.published.all().filter(category__name="World").order_by('-publish_time')[9]
#     local_11 = News.published.all().filter(category__name="World").order_by('-publish_time')[10]
#     local_12 = News.published.all().filter(category__name="World").order_by('-publish_time')[11]
#     local_13 = News.published.all().filter(category__name="World").order_by('-publish_time')[12]
#     local_14 = News.published.all().filter(category__name="World").order_by('-publish_time')[13]
#
#
#
#
#
#     context = {
#         "categories": categories,
#         "news_list": news_list,
#         "local_1": local_1,
#         "local_2": local_2,
#         "local_3": local_3,
#         "local_4": local_4,
#         "local_5": local_5,
#         "local_6": local_6,
#         "local_7": local_7,
#         "local_8": local_8,
#         "local_9": local_9,
#         "local_10": local_10,
#         "local_11": local_11,
#         "local_12": local_12,
#         "local_13": local_13,
#         "local_14": local_14,
#
#     }
#
#     return render(request, 'news/World.html', context)


# def Fan_texnikaPageView(request):
#
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:3]
#     local_1 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[0]
#     local_2 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[1]
#     local_3 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[2]
#     local_4 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[3]
#     local_5 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[4]
#     local_6 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[5]
#     local_7 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[6]
#     local_8 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[7]
#     local_9 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[8]
#     local_10 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[9]
#     local_11 = News.published.all().filter(category__name="FAn-texnika").order_by('-publish_time')[10]
#
#
#
#
#     context = {
#         "categories": categories,
#         "news_list": news_list,
#         "local_1": local_1,
#         "local_2": local_2,
#         "local_3": local_3,
#         "local_4": local_4,
#         "local_5": local_5,
#         "local_6": local_6,
#         "local_7": local_7,
#         "local_8": local_8,
#         "local_9": local_9,
#         "local_10": local_10,
#         "local_11": local_11
#
#     }
#
#     return render(request, 'news/Fan-texnika.html', context)


class SubjectNewsView(ListView):
    model = News
    template_name = 'news/Fan-texnika.html'
    context_object_name = 'fannews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='FAn-texnika')
        return news



# def SportPageView(request):
#
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:3]
#     local_1 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[0]
#     local_2 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[1]
#     local_3 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[2]
#     local_4 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[3]
#     local_5 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[4]
#     local_6 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[5]
#     local_7 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[6]
#     local_8 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[7]
#     local_9 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[8]
#     # local_10 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[9]
#     # local_11 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[10]
#
#
#
#
#     context = {
#         "categories": categories,
#         "news_list": news_list,
#         "local_1": local_1,
#         "local_2": local_2,
#         "local_3": local_3,
#         "local_4": local_4,
#         "local_5": local_5,
#         "local_6": local_6,
#         "local_7": local_7,
#         "local_8": local_8,
#         "local_9": local_9,
#         # "local_10": local_10,
#         # "local_11": local_11
#
#     }
#
#     return render(request, 'news/Sport.html', context)



class SportNewsView(ListView):
    model = News
    template_name = 'news/Sport.html'
    context_object_name = 'sportnews'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news