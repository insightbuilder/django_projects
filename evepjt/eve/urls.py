from django.urls import path
from .views import (
    hello,
    hello_name,
    hello_qp,
    post_hello,
    putKhello,
    reg_owner,
    owners,
    edit_owner,
    del_owner
)

urlpatterns = [
    path("", hello, name='hello'),
    path("hn/<str:name>", hello_name, name='hello_name'),
    path("qp/", hello_qp, name='hello_qp'),
    path("ph/", post_hello, name='post_hello'),
    path("puth/", putKhello, name='puth'),
    path("rego/", reg_owner, name='rego'),
    path("owners/", owners, name='owners'),
    path("edit_owners/<int:pk>", edit_owner, name='edit_owners'),
    path("delo/<int:pk>", del_owner, name='delo'),
]
