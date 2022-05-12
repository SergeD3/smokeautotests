# -*- coding: utf-8 -*-
import pytest
from fixture import aplc

page_link = 'http://192.168.124.56/'
_username = "s2moke_auto"
_password = "KSAAz%\"6"
# "smoke_auto", "KSAAz%\"6"


@pytest.fixture
def app(request):
    fixture = aplc.Aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth_case(app):
    app.open_page(page_link)
    app.session.login(_username, _password)
    app.session.logout()
