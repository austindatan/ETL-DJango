from django.contrib import admin
from .models import RawIMDB
from .models import CleanIMDB
admin.site.register(RawIMDB)
admin.site.register(CleanIMDB)