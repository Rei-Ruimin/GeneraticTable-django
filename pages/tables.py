import django_tables2 as tables
from .models import QuinnEmployee, DelayCode
from django_tables2.utils import A  # alias for Accessor

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name

class QuinnEmployeeTable(tables.Table):
    checkbox_column = CheckBoxColumnWithName(verbose_name="", accessor='pk')

    class Meta:
        model = QuinnEmployee
        template_name = "django_tables2/bootstrap.html"
        fields = [f.name for f in QuinnEmployee._meta.get_fields()]
        fields.remove('id')
        fields = ['checkbox_column']+ fields

class DelayCodeTable(tables.Table):
    checkbox_column = CheckBoxColumnWithName(verbose_name="", accessor='pk')

    class Meta:
        model = DelayCode
        template_name = "django_tables2/bootstrap.html"
        fields = [f.name for f in DelayCode._meta.get_fields()]
        fields.remove('id')
        fields = ['checkbox_column']+ fields
