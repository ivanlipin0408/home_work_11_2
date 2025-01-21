from scr.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_log_error(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2')\n" in captured.out
