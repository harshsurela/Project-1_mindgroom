from django.contrib import admin
from django.urls import path
from FPS import views

urlpatterns = [
    path("",views.index,name="FPS"),
    # path("user/",views.user,name="user"),
    path("useradmin/",views.useradmin,name="useradmin"),
    # path("checker/",views.checker,name="checker"),
    path("TnC/",views.TnC,name="TnC"),
    path("create/",views.create,name="create"),
    path("scanner/<int:fno>",views.scanner,name="scanner"),
    path("forgetpass/",views.forgetpass,name="forgetpass"),
    path("email-protection/",views.emailprotection,name="emailprotection"),
    path("login_user/",views.login_user,name="login_user"),
    path("cropimg/",views.cropimg,name="cropimg"),
    path("login_form/",views.login_form,name="login_form"),
    path("user_details/<str:idi>",views.user_details,name="userdetails"),
    path("signup/",views.register,name="register"),
    path("createfranchise/",views.createFranchise,name="createfranchise"),
    path("franchiseLogin/",views.franchiselogin,name="franchiselogin"),
    path("userlist/",views.userlist,name='userlist'),
    path("thankYou/",views.thanks,name='thanks'),
    path("instruction/",views.instruction,name='instruction'),
    path("nextToscan/",views.nextToscan,name='nextToscan'),
    path("download/<str:un>",views.getfiles,name="download"),
    path('del',views.delimg)
]