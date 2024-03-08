from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('split_expense.urls')),
    # Add other URL patterns as needed
]