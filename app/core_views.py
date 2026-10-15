from flask_admin.contrib.sqla import ModelView

from .permissions import AccessMixin


class PeopleView(AccessMixin, ModelView):
    can_delete = False
    page_size = 25
