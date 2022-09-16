from django.contrib import admin

from .models import Course
# , Attendance

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("c_id", "title", "semmester", "year", "seat_count", "max_seat", "quota")
    filter_horizontal = ("attend",)

# class AttendanceAdmin(admin.ModelAdmin):
#     list_display = ("s_id",)

admin.site.register(Course, CourseAdmin)
# admin.site.register(Attendance, AttendanceAdmin)
