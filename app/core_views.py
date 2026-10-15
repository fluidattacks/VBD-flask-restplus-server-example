from flask_admin.contrib.sqla import ModelView

from .permissions import AccessMixin


class PeopleView(ModelView, AccessMixin):
    can_delete = False
    page_size = 25
