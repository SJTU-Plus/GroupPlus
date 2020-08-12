from django.contrib import admin

from .models import Category, Group


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_modified'
    readonly_fields = ('last_modified',)
    fields = ('name', 'parent', 'last_modified')
    list_display = ('name', 'parent', 'last_modified')
    # def view_last_modified(self, obj: Category):
    #     return obj.last_modified.isoformat()


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_modified'
    readonly_fields = ('last_modified',)
    fields = ('name', 'number', 'category', 'last_modified')
    list_display = ('name', 'number', 'category', 'last_modified')
    list_filter = ('category',)
