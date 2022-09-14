from django.contrib import admin

from .models import Course, Attendance

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("c_id", "title", "semester", "year", "seat_count", "max_seat", "quota")

class AttendanceAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses",)

admin.site.register(Course, CourseAdmin)
admin.site.register(Attendance, AttendanceAdmin)
