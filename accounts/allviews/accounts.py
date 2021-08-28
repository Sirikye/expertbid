from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, ListView

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.views.generic.edit import UpdateView

from accounts.models import Contract, Proposal, NewUser, Project


class SignUpView(TemplateView):
    template_name = "accounts/registration/signup.html"


class LoginView(TemplateView):
    template_name = "accounts/registration/login.html"


def UserLoginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_client:
                messages.success(request, f"You are logged in as {username}")
                return redirect("client_dashboard")
            else:
                messages.success(request, f"You are logged in as {username}")
                return redirect("provider_dashboard")

        else:
            messages.info(request, f"Username or password is not correct")
    context = {}
    return render(request, "accounts/registration/login_form.html", context)


def LogoutView(request):
    logout(request)
    return redirect("home")


class ProjectListView(ListView):
    model = Project
    ordering = "-date_added"
    context_object_name = "projects_list"
    template_name = "accounts/project_list.html"


class ProposalDetailView(DetailView):
    model = Proposal
    template_name = "accounts/proposal_detail.html"


class ServiceProviderDetailView(DetailView):
    model = NewUser
    template_name = "accounts/provider_profile.html"


class ContractListView(ListView):
    model = Contract
    context_object_name = "contracts"
    ordering = "-date_created"


class ContractDetailView(DetailView):
    model = Contract
