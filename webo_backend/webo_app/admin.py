from django.contrib import admin
from .models import ResearchField,ResearchPaperDetail, Author,Affliation, AuthorKeywords,CoAuthor,Sponsor
# Register your models here.

admin.site.register(ResearchField)
admin.site.register(ResearchPaperDetail)
admin.site.register(Author)
admin.site.register(Affliation)
admin.site.register(AuthorKeywords)
admin.site.register(CoAuthor)
admin.site.register(Sponsor)
