import xadmin
from xadmin import views


class BaseSettings(object):
    enabel_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'Mary-IT课程后台管理页面'
    site_footer = 'Powered By Mary - 2020'



xadmin.site.register(views.BaseAdminView,BaseSettings)
xadmin.site.register(views.CommAdminView,GlobalSettings)