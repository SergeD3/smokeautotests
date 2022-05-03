# -*- coding: utf-8 -*-
import time
import pytest
import aplc


@pytest.fixture
def app(request):
    fixture = aplc.aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth_case(app):
    app.open_page()
    app.login("smoke_auto", "KSAAz%\"6")
    app.logout()


def test_auth_empty_case(app):
    app.open_page()
    app.login("", "")
