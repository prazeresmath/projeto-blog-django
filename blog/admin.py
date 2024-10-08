from django.contrib import admin
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')  # Correção para tupla
    list_display_links = ('name',)  # Correção para tupla
    search_fields = ('id', 'name', 'slug')  # Correção para tupla
    list_per_page = 10  # Está correto
    ordering = ('-id',)  # Correção para tupla
    prepopulated_fields = {"slug": ('name',)}  # Está correto

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')  # Correção para tupla
    list_display_links = ('name',)  # Correção para tupla
    search_fields = ('id', 'name', 'slug')  # Correção para tupla
    list_per_page = 10  # Está correto
    ordering = ('-id',)  # Correção para tupla
    prepopulated_fields = {"slug": ('name',)}  # Está correto


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',),
    }

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ['content']
    list_display = ['id', 'title', 'is_published']  # Remover 'created_by' se ele não existir no modelo
    list_display_links = ['title']  # Corrigir para lista ou tupla
    search_fields = ['id', 'slug', 'title', 'excerpt', 'content']
    list_per_page = 50
    list_filter = ['category', 'is_published']
    list_editable = ['is_published']  # Corrigir para lista ou tupla
    ordering = ['-id']  # Corrigir para lista ou tupla
    readonly_fields = ['created_at', 'updated_at', 'link']  # Remover 'created_by' e 'updated_by' se não existirem
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = ['tags', 'category']

    def link(self, obj):
        if not obj.pk:
            return '-'
        
        url_do_post = obj.get_absolute_url()
        safe_link = mark_safe(f'<a href="{url_do_post}" target="_blank">Ver post</a>')

        return safe_link

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user

        obj.save()