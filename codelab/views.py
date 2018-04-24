from django.views.generic import ListView, DetailView

from codelab.forms import CodelabForm, CodelabDetailForm
from codelab.models import Codelab, CodelabDetail
from conf.cbv import WriterCreateView, WriterUpdateView
from codelab.constants import Constant

get_codelab_list = ListView.as_view(
    model=Codelab,
    extra_context={
        "title" : Constant.CODELAB_LIST_PAGE_TITLE
    },
)
get_codelab = DetailView.as_view(
    model=Codelab,
    extra_context={
        "title" : Constant.CODELAB_PAGE_TITLE
    },
)
get_codelab_detail = DetailView.as_view(
    model=CodelabDetail,
    extra_context={
        "title" : Constant.CODELAB_DETAIL_PAGE_TITLE
    }
)

create_codelab = WriterCreateView.as_view(
    model=Codelab,
    form_class=CodelabForm ,
    template_name='codelab/codelab_form.html',
    extra_context={
        "title" : Constant.CODELAB_CREATE_PAGE_TITLE
    },
)
create_codelab_detail = WriterCreateView.as_view(
    model=CodelabDetail,
    form_class=CodelabDetailForm,
    template_name='codelab/codelabdetail_form.html',
    extra_context={
        "title" : Constant.CODELAB_DETAIL_CREATE_PAGE_TITLE
    },
)
update_codelab = WriterUpdateView.as_view(
    model=Codelab,
    form_class=CodelabForm,
    template_name='codelab/codelab_form.html',
    extra_context={
        "title" : Constant.CODELAB_UPDATE_PAGE_TITLE
    },
)
update_codelab_detail = WriterUpdateView.as_view(
    model=CodelabDetail,
    form_class=CodelabDetailForm,
    template_name='codelab/codelabdetail_form.html',
    extra_context={
        "title" : Constant.CODELAB_UPDATE_DETAIL_PAGE_TITLE
    },
)