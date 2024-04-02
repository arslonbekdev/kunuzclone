from django.contrib import admin

from news_app.models import Category, News,ContactData,Contact

# Register your models here.

 # 1 - method
# admin.site.register(Category)
# admin.site.register(News)


# 2 - method
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'category']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {"slug": ('title', )}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

admin.site.register(ContactData)
admin.site.register(Contact)