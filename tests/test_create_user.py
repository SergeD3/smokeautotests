# -*- coding: utf-8 -*-
import pytest
from model.user import AddUser
from fixture import aplc
import time


@pytest.fixture
def app(request):
    fixture = aplc.Aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_crt_users(app):
    app.open_page()
    app.session.login("smoke_auto", "KSAAz%\"6")
    app.users.open_create_window()
    # app.users.fill_users_form(AddUser('Смоковый юзер - автотест', 'smoke_autotest1', 'kub3auto@ya.ru', '+79893455443'))
#    app.session.logout()
