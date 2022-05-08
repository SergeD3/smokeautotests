# -*- coding: utf-8 -*-
import pytest
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
    time.sleep(2)
    app.users.open_create_user()
    app.session.logout()
