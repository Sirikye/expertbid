from django.urls import path, include

from accounts import views

from accounts.allviews import client, provider, accounts

urlpatterns = [
    # path("", home, name="home"),
    path("", views.home, name="home"),
    # Dashboard urls <Client>
    path(
        "dashboard/client/",
        client.ClientDashboard.as_view(),
        name="client_dashboard",
    ),
    # Project Urls Here <Client>
    path("projects/", accounts.ProjectListView.as_view(), name="projects"),
    path(
        "project/create/",
        client.ProjectCreateView.as_view(),
        name="create-project",
    ),
    path(
        "projects/project/<int:pk>/",
        client.ProjectDetailView.as_view(),
        name="project_detail",
    ),
    path(
        "update-project/<int:pk>/",
        client.ProjectUpdateView.as_view(),
        name="project_update",
    ),
    path(
        "projects/project/<int:pk>/delete",
        client.ProjectDeleteView.as_view(),
        name="project_delete",
    ),
    # Dashboard urls <Service Provider>
    path(
        "dashboard/service-provider/",
        provider.ProviderDashboard.as_view(),
        name="provider_dashboard",
    ),
    # Proposal Views here
    path(
        "project/<int:pk>/create-proposal/",
        provider.ProposalCreateView.as_view(),
        name="create_proposal",
    ),
    path(
        "proposals/",
        client.ProposalListView.as_view(),
        name="proposals",
    ),
    path(
        "dashboard/client/freelancers/",
        client.ServiceProviderListView.as_view(),
        name="freelancers",
    ),
    path(
        "service-provider/<int:pk>/",
        accounts.ServiceProviderDetailView.as_view(),
        name="provider_profile",
    ),
    path(
        "proposal/<int:pk>/",
        accounts.ProposalDetailView.as_view(),
        name="proposal_detail",
    ),
    path(
        "update-proposal/<int:pk>/",
        provider.ProposalUpdateView.as_view(),
        name="proposal_update",
    ),
    path(
        "dashboard/contracts/",
        accounts.ContractListView.as_view(),
        name="contract_list",
    ),
    path(
        "proposal/<int:pk>/create-contract/",
        client.ContractCreateView.as_view(),
        name="contract_create",
    ),
    path(
        "contract/<int:pk>/",
        accounts.ContractDetailView.as_view(),
        name="contract_detail",
    ),
]
