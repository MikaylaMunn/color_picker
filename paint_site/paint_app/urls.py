from django.urls import path
from paint_app.views import ColorPickerView


urlpatterns = [
    # paint_app/
    path('',  ColorPickerView.as_view(), name='paint'),
]