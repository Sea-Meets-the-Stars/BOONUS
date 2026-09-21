""" Smoke tests: the package installs and imports cleanly """

def test_import():
    import boonus


def test_version():
    import boonus
    assert isinstance(boonus.__version__, str)
