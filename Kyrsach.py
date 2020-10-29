'''
Программа должна предоставлять средства для перевода целых чисел, 
записанных в системе счисления с основанием q (2<=q<=16) 
в систему с основанием p (2<=p<=16). 
Операции: 
• ввод числа-источника и основания его системы 
счисления с проверкой корректности вводимых данных; 
• перевод целого числа из одной системы счисления в другую 
(при переводе числа из q-ой системы в 10-ую использовать схему Горнера); 
• вывод числа, имеющего заданную систему счисления в виде 
последовательности символов, используемых в системе счисления 
в основания его системы счисления с проверкой корректности вводимых данных.

'''

#Функция выбора системы исчисления
def GetNumSystem():
    while True:
        try:
            numSystem = input('Выберите систему исчисления: BIN, OCT, DEC, HEX : ')
            
            if numSystem == 'BIN':
                return 2
            elif numSystem == 'OCT':
                return 8
            elif numSystem == 'DEC':
                return 10
            elif numSystem == 'HEX':
                return 16
            else:
                print('Такого варианта нет...')

        except ValueError:
            print('Ошибка введенного значения...')
       

# s - start (Начальная СС)
# e - end (Целевая СС)
# v - value (Введенное значение)
def perevod(v, s, e):
   
    #print("Начальная СС: ", s)
    #print("Конечная СС: ", e)
    #print("Значение: ", v)

    # ИЗ десятичной
    if s == 10: 
        if e == 2:
            print(bin(int(v)))
           # return bin(v)
        elif e == 8:
            print(oct(int(v)))
        elif e == 10:
            print(v)
        elif e == 16:
            print(hex(int(v)))

    # ИЗ двоичной
    elif s == 2:
        if e == 2:
            print(v)
        elif e == 8:
            print( oct(int(str(v), s)) )
        elif e == 10:
            print( int(str(v), s) )
        elif e == 16:
            print( hex(int(str(v), s)) )
    
    # ИЗ восьмеричной
    elif s == 8:
        if e == 2:
            print( bin(int(str(v), s)) )
        elif e == 8:
            print( v )
        elif e == 10:
            print( int(str(v), s) )
        elif e == 16:
            print( hex(int(str(v), s)) )
    
    # ИЗ шестадцатеричной
    elif s == 16:
        if e == 2:
            print( bin(int(str(v), s)) )
        elif e == 8:
            print( oct(int(str(v), s)) )
        elif e == 10:
            print( int(str(v), s) )
        elif e == 16:
            print( v )

def main():
    print('Исходная система исчисления - ')
    fNumSystem = GetNumSystem()  # Получаем исходную систему исчисления

    value = input('Введите значение: ')  # Получаем исходное число



    print('Система исчисления в которую необходимо перевести число:')

    sNumSystem = GetNumSystem()  # Получаем систему исчисления в которую необходимо перевести

    print('Число: ')
    #print(value)
    perevod(value, fNumSystem, sNumSystem)
    



main()




