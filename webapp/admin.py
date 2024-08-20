from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portfolio, Contact

# Register your models here.

# Home
admin.site.register(Home)


# Portfolio
admin.site.register(Portfolio)
# contact messages
admin.site.register(Contact)

# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     inlines = [
        ProfileInline,
    ]

# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]

