# -*- coding: utf-8 -*-
import pytest
from model.user import AddUser
from fixture import aplc

page_link = 'http://192.168.124.56/'
_username = "smoke_auto"
_password = "KSAAz%\"6"


@pytest.fixture
def app(request):
    fixture = aplc.Aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_crt_users(app):
    app.open_page(page_link)
    app.session.login(_username, _password)
    app.users.open_create_window()
    app.users.fill_users_form(AddUser('Смоковый юзер - автотест', 'smoke_autotest1', 'kub3auto@ya.ru', '+79893455443'))
    app.users.check_usergroup()
    app.session.logout()
