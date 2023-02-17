from django.urls import path


from applications.chr_models.views import DataBaseInfo

urlpatterns = [
    path('db_data/', DataBaseInfo.as_view()),


]
