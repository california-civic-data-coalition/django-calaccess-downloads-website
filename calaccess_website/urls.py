from django.conf.urls import url
from calaccess_website import views


urlpatterns = [
    # The homepage
    url(
        r'^$',
        views.Home.as_view(),
        name="home",
    ),

    # Version archive views
    url(
        r'^versions/$',
        views.VersionArchiveIndex.as_view(),
        name="version_archive_index",
    ),
    url(
        r'^versions/(?P<year>[0-9]{4})/$',
        views.VersionYearArchiveList.as_view(),
        name="version_archive_year"
    ),
    url(
        r'^versions/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.VersionMonthArchiveList.as_view(),
        name="version_archive_month"
    ),
    url(
        r'^versions/latest/$',
        views.LatestVersion.as_view(),
        name='version_latest_redirect'
    ),
    url(
        r'^versions/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<release_epochtime>[0-9]+)/$',
        views.VersionDetail.as_view(),
        name="version_detail"
    ),

    # Raw data file archive views
    url(
        r'^raw-data-files/$',
        views.RawDataFileList.as_view(),
        name='rawdatafiles_list'
    ),
    url(
        r'^raw-data-files/(?P<file_name>\w+)/$',
        views.RawDataFileDetail.as_view(),
        name='rawdatafile_detail',
    ),
]
