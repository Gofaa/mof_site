from django.contrib import admin
from .models import ActiveStudents, InactiveStudents

# Register your models here.


admin.site.register(ActiveStudents)
admin.site.register(InactiveStudents)
