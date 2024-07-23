from django.contrib import admin
from .models import Home , About, Porfile, Portfolio, Category, Skill

# Register your models here.
admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model= Porfile
    extra= 1
admin.site.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines= [
        ProfileInline,
    ]

admin.site.register(Skill)
class SkillInline(admin.TabularInline):
    model= Skill
    extra =2
        
        
        
            
admin.site.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    inlines=[
        SkillInline,
    ]
    
admin.site.register(Portfolio)

    
    