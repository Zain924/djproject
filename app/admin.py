from django.contrib import admin
from app.models import contact ,Projects,about,CV,Images

# Register your models here.

admin.site.register(contact)
admin.site.register(Projects)
admin.site.register(CV)
admin.site.register(Images)


class AboutAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Assuming you want to display the entry with id=1, change it as needed.
        return about.objects.filter(id=1)

admin.site.register(about, AboutAdmin)