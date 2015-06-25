from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^foobar/$', 'serializer_test.views.sample_view_2', name='sample-view-2'),
    url(r'^$', 'serializer_test.views.sample_view', name='sample-view'),
)
