from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from .ui import UserAddWindow


class ContentTypePack(ObjectPack):
    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_desktop = True


class UserPack(ObjectPack):
    model = User
    add_window = edit_window = UserAddWindow
    add_to_desktop = True


class GroupPack(ObjectPack):
    model = Group
    add_window = edit_window = ModelEditWindow.fabricate(model)
    add_to_desktop = True


class PermissionPack(ObjectPack):
    model = Permission
    add_window = edit_window = ModelEditWindow.fabricate(
        model,
        field_list=['name', 'content_type', 'codename']
    )
    add_to_desktop = True
