from django.contrib import admin
from import_export import resources
from import_export.fields import Field
from .models import Todo
# Register your models here.
admin.site.register(Todo)

class TodoResource(resources.ModelResource):
    user = Field()
    class Meta:
        model = Todo
        exclude = ('id')
        fields = ('user','text','is_completed','created_time','last_updated')
        widgets = {
        'created_time': {'format': '%d-%m-%Y %H:%M:%S'},
        'last_updated': {'format': '%d-%m-%Y %H:%M:%S'},
        }
    def dehydrate_user(self,todo):
        return '%s' % (todo.user.username)
    def dehydrate_is_completed(self,todo):
        if todo.is_completed:
            return 'Completed'
        else: return 'Not Completed'