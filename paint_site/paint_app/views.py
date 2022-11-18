from django.shortcuts import render
from django.views import View

from paint_app.forms import ColorPickerForm


# Create your views here.
class ColorPickerView(View):
    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            "form": form,
            "red": 255,
            "green": 255,
            "blue": 255,
        }

        return render(request=request, template_name="paint.html", context=context)

    # needed to get the users input
    def post(self, request):
        """Display the user's chosen color"""
        # POST data sent back so we can see what color they picked
        form = ColorPickerForm(request.POST)
        # accesses the data in the QueryDict
        red = int(request.POST["red_amount"])
        green = int(request.POST["green_amount"])
        blue = int(request.POST["blue_amount"])

        context = {
            "form": form,
            "red": red,
            "green": green,
            "blue": blue,
        }

        return render(request=request, template_name="paint.html", context=context)

    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            "form": form,
            "red": 255,
            "green": 255,
            "blue": 255,
        }

        return render(request=request, template_name="paint.html", context=context)
