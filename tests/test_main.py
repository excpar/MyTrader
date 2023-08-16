"""Test main"""
import sys

import pytest

from mytrader import main


def test_help(mocker, capsys):
    """test help command"""
    args = ['mytrader', '-h']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        main.main()

    assert ex.value.code == 0
    outerr = capsys.readouterr()
    assert '-s SOURCE' in outerr.out
    assert '-d DEST' in outerr.out

def test_only_pass_source(mocker, capsys):
    """test only pass -s """
    args = ['mytrader', '-s', 'foo']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        main.main()

    assert ex.value.code == 2
    outerr = capsys.readouterr()
    assert 'the following arguments are required: -d' in outerr.err

def test_only_pass_dest(mocker, capsys):
    """test only pass -d"""
    args = ['mytrader', '-d', 'foo']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        main.main()

    assert ex.value.code == 2
    outerr = capsys.readouterr()
    assert 'the following arguments are required: -s' in outerr.err

def test_main(mocker):
    """test cmdline, and everything is fine."""
    args = ['mytrader', '-s', 'foo', '-d', 'bar']
    mocker.patch.object(sys, 'argv', args)
    mock_count = mocker.patch('mytrader.cmdline.count')
    main.main()
    mock_count.assert_called_once()
