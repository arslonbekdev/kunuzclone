from .models import News, Category, ContactData

def latest_news(request):
    latest_news = News.published.all().order_by("-publish_time")[:10]
    categories = Category.objects.all()
    contact_data = ContactData.objects.all()
    context ={
        'latest_news': latest_news,
        'categories': categories,
        'contact_data': contact_data,
    }
    return context
