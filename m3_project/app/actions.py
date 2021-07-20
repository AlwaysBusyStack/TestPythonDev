from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .controller import observer
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
    add_window = edit_window = ModelEditWindow.fabricate(model=model)
    add_to_desktop = True


class PermissionPack(ObjectPack):
    model = Permission
    # Если хотим создать поле выбора словаря - необходимо в
    # фабричный метод передавать нашего наблюдателя
    # иначе мы не сможем найти экшнпак для создания поля
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer
    )
    add_to_desktop = True
