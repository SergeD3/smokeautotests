# -*- coding: utf-8 -*-
import pytest
from fixture import aplc
from datetime import datetime
from pathlib import Path

page_link = 'http://192.168.124.56/'
_username = "smoke_auto"
_password = "KSAAz%\"6"  # "smoke_auto", "KSAAz%\"6"
date = datetime.today().strftime('%m-%d-%y %H-%M-%S')
filename = 'TestFullPage_' + date + ".png"
path_file = Path(Path.home(), 'Desktop', 'screenshots_smoke', filename)


@pytest.fixture
def app(request):
    fixture = aplc.Aplcs()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth_case(app):
    app.open_page(page_link)
    app.session.login(_username, _password)
    app.take_screen(path_file)
    app.session.logout()
