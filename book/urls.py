from django.conf.urls import url
from book import views

book_urlpatterns = [url(r'^publishers$', views.PublisherList.as_view(), name="publisher"),
                    url(r'^authors$', views.AuthorList.as_view(), name="author"),
                    url(r'^author_detail/(?P<pk>\d+)', views.AuthorDetailView.as_view(),
                        name="author_detail")]
