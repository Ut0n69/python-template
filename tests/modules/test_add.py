from python_project_template.modules.add import add


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
