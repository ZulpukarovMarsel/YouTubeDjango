from django.contrib import admin
from .models import User, Channel

admin.site.register(User)


@admin.register(Channel)
class ChanelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "owner", "subscribers_list", "created_date")
    search_fields = ("name", "author", "created_date")

    def subscribers_list(self, obj):
        return ", ".join([str(subscriber) for subscriber in obj.subscribers.all()])

    subscribers_list.short_description = "Subscribers"