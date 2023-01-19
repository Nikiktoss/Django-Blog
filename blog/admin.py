from django.contrib import admin
from .models import Note, Action


admin.site.site_header = "Администрирование сайта MyBlog"
admin.site.site_title = "Административная панель сайта MyBlog"


class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "date_create", "date_update")
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ("title", "slug")
    ordering = ("-date_create",)
    fields = (("title", "slug"), "content")


class ActionAdmin(admin.ModelAdmin):
    list_display = ("action", "date_create")


admin.site.register(Action, ActionAdmin)
admin.site.register(Note, NoteAdmin)
