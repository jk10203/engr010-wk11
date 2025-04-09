import pytest
import numpy as np
import my_module as mm

def test_two_sum_valid_case():
    result = mm.two_sum([2, 7, 11, 15], 9)
    assert set(result) == {0, 1}

def test_chooser_returns_valid_item():
    items = {"red", "blue", "white", "black"}
    chooser = mm.Chooser(items)
    chosen = chooser.choose()
    assert chosen in items

def test_generate_plot_runs(monkeypatch):
    #monkeypatch plt.show --> avoid opening GUI window
    import matplotlib.pyplot as plt
    monkeypatch.setattr(plt, "show", lambda: None)
    
    def square(x):
        return x**2

    xvals = np.linspace(-10, 10, 100)
    mm.generate_plot(square, xvals)  #run without error
