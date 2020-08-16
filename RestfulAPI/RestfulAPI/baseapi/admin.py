from django.contrib import admin

from .models import *

admin.site.site_title = " پنل مدیریت دیتابیس"
admin.site.site_header = "خوش آمدید"


admin.site.register(Customer)
admin.site.register(MobileInfo)