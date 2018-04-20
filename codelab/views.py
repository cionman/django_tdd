from django.views.generic import ListView, DetailView

from codelab.forms import CodelabForm, CodelabDetailForm
from codelab.models import Codelab, CodelabDetail
from conf.cbv import WriterCreateView, WriterUpdateView

get_codelab_list = ListView.as_view(model=Codelab)
get_codelab = DetailView.as_view(model=Codelab)
get_codelab_detail = DetailView.as_view(model=CodelabDetail)
create_codelab = WriterCreateView.as_view(
    model=Codelab
    , form_class=CodelabForm
    , template_name='codelab/codelab_form.html')
create_codelab_detail = WriterCreateView.as_view(
    model=CodelabDetail
    , form_class=CodelabDetailForm
    , template_name='codelab/codelabdetail_form.html')
update_codelab = WriterUpdateView.as_view(
    model=Codelab
    , form_class=CodelabForm
    , template_name='codelab/codelab_form.html')
update_codelab_detail = WriterUpdateView.as_view(
    model=CodelabDetail
    , form_class=CodelabDetailForm
    , template_name='codelab/codelabdetail_form.html')