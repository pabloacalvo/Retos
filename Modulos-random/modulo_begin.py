import begin

@begin.start
def main(param_1, param_2, param_3='default'):
    """
    Begin ayuda a crear scripts de linea de comandos, con argumentos posicionales y opcionales
    con ayuda automatica
    """
    print(f'Parametro 1:{param_1}' )
    print(f'Parametro 2:{param_2}' )
    print(f'Parametro 3:{param_3}' )