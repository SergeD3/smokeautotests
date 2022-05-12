# -*- coding: utf-8 -*-
import pytest
from fixture import aplc

_username = "s2moke_auto"
_password = "KSAAz%\"6"


@pytest.fixture
def app(request):
    fixture = aplc.Aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth_case(app):
    app.open_page()
    app.session.login(_username, _password)  # "smoke_auto", "KSAAz%\"6"
    app.session.logout()
