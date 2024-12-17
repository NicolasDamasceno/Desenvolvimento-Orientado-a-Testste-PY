# Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de
# término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos.
# O procedimento deve retornar, também por parâmetro, a duração do jogo em
# horas e minutos, considerando que o tempo máximo de duração de um jogo é
# de 24 horas e que o jogo pode começar em um dia e terminar no outro.

def horario(horaInicio, horaTermino):
    if type(horaInicio) != tuple or type(horaTermino) != tuple:
        return Exception
    
    if len(horaInicio) != 2 or len(horaTermino) != 2:
        return Exception
    
    if not((isinstance(horaInicio[0],int)) and (isinstance(horaInicio[1],int)) and 
           isinstance(horaTermino[0],int) and isinstance(horaTermino[1], int)):
        return Exception
    
    
    if horaInicio[0] < 0 or horaInicio[0] > 23 or horaInicio[1] < 0 or horaInicio[1] > 59:
        return Exception
    
    if horaTermino[0] < 0 or horaTermino[0] > 23 or horaTermino[1] < 0 or horaTermino[1] > 59:
        return Exception
     
    # Transformando os horários em minutos totais
    minutosInicio = (horaInicio[0]*60) + horaInicio[1]
    minutosFinal = (horaTermino[0]*60) + horaTermino[1]

    # Ajustando caso se passe um dia inteiro
    if minutosFinal < minutosInicio:
        minutosFinal += 24*60

    duracaoMinutos = minutosFinal - minutosInicio

    horaFinal = duracaoMinutos // 60
    minutosFinal = duracaoMinutos % 60

    return (horaFinal, minutosFinal)
    
# Valores Inválidos
assert horario([6,50],(8,40)) == Exception
assert horario((7,0),[9,40]) == Exception
assert horario((7.45,10),(9,0)) == Exception
assert horario((7,45.1),(8,30)) == Exception
assert horario((8,10.1),(9.0)) == Exception
assert horario((7,10),(8.1,20)) == Exception
assert horario((7,10),(8,15.5)) == Exception
assert horario((7,),(8,10)) == Exception
assert horario((6,50),(7,)) == Exception
assert horario((24,10),(2,5)) == Exception
assert horario((22,60),(23,40)) == Exception
assert horario((22,0),(25,10)) == Exception
assert horario((22,0),(23,65)) == Exception

#Valores Válidos
assert horario((0,0),(6,0)) == (6,0)
assert horario((22,37),(3,31)) == (4,54)

print('Gotcha! Testes okay')