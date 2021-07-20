import objectpack.models
from m3_ext.ui.fields import ExtDictSelectField
from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):
    """
    Созданное окно для работы с пользователем
    """
    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'Username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )

        self.field__password = ext.ExtStringField(
            label=u'Password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )

        self.field__first_name = ext.ExtStringField(
            label=u'First name',
            name='first_name',
            anchor='100%'
        )

        self.field__last_name = ext.ExtStringField(
            label=u'Last name',
            name='last_name',
            anchor='100%'
        )

        self.field__email_address = ext.ExtStringField(
            label=u'Email address',
            name='email',
            anchor='100%'
        )

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Superuser status',
            name='is_superuser'
        )

        self.field__is_stuff = ext.ExtCheckBox(
            label=u'Staff status',
            name='is_staff',
        )

        self.field__is_active = ext.ExtCheckBox(
            label=u'Active',
            name='is_active',
        )

        self.field__date_joined = ext.ExtDateField(
            label=u'Date joined',
            name='date_joined',
            anchor='100%',
            format='d.m.Y'
        )

        self.field__last_login = ext.ExtDateField(
            label=u'Last login',
            name='last_login',
            anchor='100%',
            format='d.m.Y'
        )

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__first_name,
            self.field__last_name,
            self.field__email_address,
            self.field__is_superuser,
            self.field__is_stuff,
            self.field__is_active,
            self.field__date_joined,
            self.field__last_login
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
