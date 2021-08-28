from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from accounts.models import NewUser, Project, Proposal
from accounts.forms import ProviderSignUpForm, ProposalForm


class ProviderSignUpView(CreateView):
    model = NewUser
    form_class = ProviderSignUpForm
    template_name = "accounts/registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Work"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_provider = True
        user.save()
        login(self.request, user)
        return redirect("provider_dashboard")


class ProviderDashboard(ListView):
    model = Project
    context_object_name = "projects_list"
    ordering = ("-date_added",)
    template_name = "accounts/provider/pro_dashboard.html"


class ProposalCreateView(CreateView):
    model = Proposal
    form_class = ProposalForm
    template_name = "accounts/provider/proposal_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.project_id = self.kwargs["pk"]
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProposalUpdateView(UpdateView):
    model = Proposal
    template_name = "accounts/provider/proposal_form.html"
    fields = [
        "body",
    ]
