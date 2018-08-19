import os

from glue.utils.qt import get_qapp  # noqa

app = None


def pytest_configure(config):
    global app
    app = get_qapp()


def pytest_unconfigure(config):
    global app
    app = None
