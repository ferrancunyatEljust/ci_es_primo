from src.funciones import es_primo

def test_primo_1():
    assert es_primo(1) == False

def test_es_primo_2():
    assert es_primo(2) == True

def test_es_primo_negativo():
    assert es_primo(-10) == False

def test_es_primo_primo_mayor_2():
    assert es_primo(29) == True

def test_es_primo_compuesto():
    assert es_primo(10) == False

