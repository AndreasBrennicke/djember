from .views import BookApiView, BookRudView
from django.conf.urls import url

urlpatterns = [
    url(r"^$", BookApiView.as_view(), name="book-create"),
    url(r'^(?P<id>\d+)', BookRudView.as_view(), name='book-rud')
]
