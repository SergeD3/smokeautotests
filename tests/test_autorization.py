# -*- coding: utf-8 -*-
import pytest
from fixture import aplc


@pytest.fixture
def app(request):
    fixture = aplc.Aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth_case(app):
    app.open_page()
    app.session.login("smoke_auto", "KSAAz%\"6")  # "smoke_auto", "KSAAz%\"6"
    app.session.logout()