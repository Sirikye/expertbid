from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    detail,
)

from accounts.models import Contract, NewUser, Project, Proposal
from accounts.forms import ClientSignUpForm, ProposalForm, ProjectForm


class ClientSignUpView(CreateView):
    model = NewUser
    form_class = ClientSignUpForm
    template_name = "accounts/registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Talent"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_client = True
        user.save()
        login(self.request, user)
        return redirect("client_dashboard")


class ClientDashboard(ListView):
    model = Project
    ordering = ("-date_added",)
    context_object_name = "projects"
    template_name = "accounts/client/client_dashboard.html"


"""
A client creates a project.
Project related views
"""


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "accounts/client/project_form.html"

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "accounts/client/project_form.html"
    fields = [
        "title",
        "text",
    ]


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/"


"""
Proposal views here
"""


class ProposalListView(ListView):
    model = Proposal
    context_object_name = "proposals"
    ordering = ("-date_added",)
    template_name = "accounts/client/proposals.html"


class ServiceProviderListView(ListView):
    model = NewUser
    context_object_name = "service_providers"
    template_name = "accounts/client/provider_list.html"


class ContractCreateView(CreateView):
    model = Contract
    fields = [
        "title",
        "body",
    ]
    template_name = "accounts/client/contract_form.html"

    def form_valid(self, form):
        form.instance.client = self.request.user
        form.instance.proposal_id = self.kwargs["pk"]
        return super().form_valid(form)
