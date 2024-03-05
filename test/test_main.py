from ..main import check_guess, print_word

def test_check_guess():
    assert check_guess("hello", "hello") == "GGGGG"
    assert check_guess("system", "policy") == "RYRRRR"
    assert check_guess("support", "general") == "RRRRRYR"
    assert check_guess("website", "program") == "RRRRRRR"
    assert check_guess("informed", "quantity") == "YYRRRRRR"

def test_print_word():
    assert print_word("GGGGG", "hello", 0) == '[green]h[/green][green]e[/green][green]l[/green][green]l[/green][green]o[/green]'
    assert print_word("GGGGRY", "helloi", 0) == '[green]h[/green][green]e[/green][green]l[/green][green]l[/green][red]o[/red][yellow]i[/yellow]'
    assert print_word("GGGGR", "hello", 0) == '[green]h[/green][green]e[/green][green]l[/green][green]l[/green][red]o[/red]'
    assert print_word("RGGGG", "hello", 0) == '[red]h[/red][green]e[/green][green]l[/green][green]l[/green][green]o[/green]'
    assert print_word("YGGGG", "hello", 0) == '[yellow]h[/yellow][green]e[/green][green]l[/green][green]l[/green][green]o[/green]'


def test_get_guess(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "magic")
    guess = input("PLease make a 5-letter guess: ")
    assert guess == "magic"

    monkeypatch.setattr("builtins.input", lambda _: "cargo")
    guess = input("PLease make a 5-letter guess: ")
    assert guess == "cargo"

    monkeypatch.setattr("builtins.input", lambda _: "helpme")
    guess = input("PLease make a 6-letter guess: ")
    assert guess == "helpme"

    monkeypatch.setattr("builtins.input", lambda _: "value")
    guess = input("PLease make a 5-letter guess: ")
    assert guess == "value"

    monkeypatch.setattr("builtins.input", lambda _: "magic1")
    guess = input("PLease make a 6-letter guess: ")
    assert guess == "magic1"