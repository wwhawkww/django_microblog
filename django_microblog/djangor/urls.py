from django.conf.urls import patterns, url,include
from django.views.generic import ListView


from djangor.models import Entry
from djangor.forms import EntryForm
from djangor.views import AddEntryView
from registration.views import register


urlpatterns = patterns('',
    # List view for all posts:
    url(r'^$',
        ListView.as_view(
            queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="djangor/entry_list.html"
        ),
        name="entry_list"),
    url(r'^add/$',
        AddEntryView.as_view(
            model=Entry,
            form_class=EntryForm,
            template_name="djangor/entry_form.html",
            success_url="/",
        ),
        name="add_entry"),
    url(r'^success/$',ListView.as_view( queryset=Entry.objects.all(),
            context_object_name="entries",
            template_name="registration/registration_complete.html",),
            name = "register_success"),
)