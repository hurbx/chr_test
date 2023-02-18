from django.urls import path


from applications.chr_models.views import DataBaseInfo, TableInfo

urlpatterns = [
    path('db_data/', DataBaseInfo.as_view()),
    path('table_data/', TableInfo.as_view()),


]
