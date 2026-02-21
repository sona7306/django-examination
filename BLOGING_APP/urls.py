from django.urls import path

from BLOGING_APP import views, blogviews, adminviews

urlpatterns = [
    path("", views.index, name='index'),
    path("dash",views.dash,name='dash'),
    path("admin",views.admin,name='admin'),
    path("blogger",views.blogger,name='blogger'),
    path("login_view",views.login_view,name='login_view'),
    path("blogger_add",views.blogger_add,name='blogger_add'),
    path("my_profile",views.my_profile,name='my_profile'),
    path("blogger_edit",blogviews.blogger_edit,name="blogger_edit"),
    path("blogpost_add",blogviews.blogpost_add,name="blogpost_add"),
    path("blogpost_list",blogviews.blogpost_list,name="blogpost_list"),
    path("blogpost_delete/<int:id>/", blogviews.blogpost_delete, name="blogpost_delete"),
    path("blogpost_update/<int:id>/", blogviews.blogpost_update, name="blogpost_update"),
    path("blogpost_lists",adminviews.blogpost_lists,name="blogpost_lists"),
    path("blogposts_lists",blogviews.blogposts_lists,name="blogposts_lists"),
    path("bloggers_list",adminviews.bloggers_list,name="bloggers_list"),
    path("bloggers_delete/<int:id>/", adminviews.bloggers_delete, name="bloggers_delete"),
    path("Log_out",adminviews.Log_out,name="Log_out"),
    path("Log_out",blogviews.Log_out,name="Log_out"),

]
