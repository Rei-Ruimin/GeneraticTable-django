from pickle import TRUE
from urllib import request
from django.shortcuts import redirect, render
from django_tables2 import SingleTableView

from pages.forms import QuinnEmployeeForm, DelayCodeForm
from .models import QuinnEmployee, DelayCode
from .tables import QuinnEmployeeTable, DelayCodeTable
from django.contrib import messages
from django.forms.models import model_to_dict

page_model_dict = {"quinn_employee":QuinnEmployee, "delay_code":DelayCode}
page_form_dict = {"quinn_employee":QuinnEmployeeForm, "delay_code":DelayCodeForm}

def get_modelform_with_init_val(page_name, id):
    model = page_model_dict[page_name]
    object = model.objects.get(id=id)
    if page_name == 'quinn_employee':
        model_form = QuinnEmployeeForm(instance=object)
    elif page_name == "delay_code":
        model_form = DelayCodeForm(instance=object)
    return model_form



def delete_row(request):
    if request.method == 'GET':
        url = request.META["HTTP_REFERER"]
        delete_list = request.GET.getlist('id_list[]')
        page = request.GET.get('page')
        model = page_model_dict[page]
        model.objects.filter(id__in=delete_list).delete()
        return redirect(url)

def detail_popup(request):
    # edit
    if request.method == "POST":
        context = {}
        url = request.META["HTTP_REFERER"]
        page_name = url.split('/')[3]
        edit_id = request.POST.get('show-edit-id')
        context['id'] = edit_id
        context["model_form"] = get_modelform_with_init_val(page_name, edit_id)
        context['type'] = 'edit'
        return render(request=request, template_name="pages/detail_popup.html", context=context)
    #add
    elif request.method == "GET":
        url = request.META["HTTP_REFERER"]
        page_name = url.split('/')[3]
        context = {}
        context['model_form'] = page_form_dict[page_name]
        context['type'] = 'add'
        return render(request=request, template_name="pages/detail_popup.html", context=context)

class QuinnEmployeeListView(SingleTableView):
    model = QuinnEmployee
    table_class = QuinnEmployeeTable
    template_name = 'pages/tables/quinn_employee.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get("popup-add-btn"):
            model_form =  QuinnEmployeeForm(request.POST)
            if model_form.is_valid():
                model_form.save()
                url = request.META["HTTP_REFERER"]
                return redirect(url)
            else:
                messages.error(request, 'Error saving form')
        elif request.POST.get("popup-edit-btn"):
            id = request.POST.get("edit-id")
            model_form =  QuinnEmployeeForm(request.POST, instance=QuinnEmployee.objects.get(id=id))
            if model_form.is_valid():
                model_form.save()
                url = request.META["HTTP_REFERER"]
                return redirect(url)
            else:
                messages.error(request, 'Error saving form')
            
class DelayCodeListView(SingleTableView):
    model = DelayCode
    table_class = DelayCodeTable
    template_name = 'pages/tables/delay_code.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get("popup-add-btn"):
            model_form =  DelayCodeForm(request.POST)
            if model_form.is_valid():
                model_form.save()
                url = request.META["HTTP_REFERER"]
                return redirect(url)
            else:
                messages.error(request, 'Error saving form')
        elif request.POST.get("popup-edit-btn"):
            id = request.POST.get("edit-id")
            model_form =  DelayCodeForm(request.POST, instance=DelayCode.objects.get(id=id))
            if model_form.is_valid():
                model_form.save()
                url = request.META["HTTP_REFERER"]
                return redirect(url)
            else:
                messages.error(request, 'Error saving form')