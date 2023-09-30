from django.contrib import admin
from .models import Car,CarPlan,PostRates, Posts, Modules, Students

# Register your models here.
admin.site.register(Car)
admin.site.register(CarPlan)
admin.site.register(Posts)
admin.site.register(PostRates)
admin.site.register(Modules)
admin.site.register(Students)