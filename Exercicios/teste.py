def dividir (a: int, b: int):
    """
    função para dividir dois números
    """
    try:
        return a/b 
    except ZeroDivisionError: 
        print('Você tentou dividir por zero!!!!!')
    except TypeError:
        print('Você tentou uma letra!!!')
    finally:
        print('Parabéns!!!!')

print(dividir(12, 2))
(dividir(12, 0))
(dividir(12, 'a'))