from django.urls import path, include
from . import views

"""from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
import photo.views
import accounts.views
"""

urlpatterns = [
    path('blog/<int:blog_id>', views.detail, name="detail"),
]