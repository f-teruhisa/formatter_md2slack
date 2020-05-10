"""pytest and fixtures for main.py"""
import pytest

@pytest.fixture()
def test_txtfile(tmpdir):
    """
    main.format_textfile(txtfile) unittest
    :param tmpdir: fixtures of txtfile
    :return formatted_txtfile: , slack notification request:
    """
    tmpfile = tmpdir.join('text.txt')

    with tmpfile.open('w') as txt_file:
        txt_file.write('- [ ] [TEST-1] test1\n\t- [x] test2')

    yield tmpfile

    tmpfile.remove()
