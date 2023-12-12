from prikon_c import spotrebic
def main():
    print('*---------------------------------------------*')
    print('Program vytvořil Aleš Toman IT4, dne 16.11.2023')
    print('*---------------------------------------------*')
    print('----------------------------')
    print('Jestli chceš program ukončit tak zadej q/Q.')
    print('----------------------------')
    while True:
        napeti = input('zadej napětí(U):')
        if napeti.upper() == 'Q':
            break
        proud = input('zadej proud(I):')
        if proud.upper() == 'Q':
            break
        try:
            napeti = float(napeti)
            proud = float(proud)
            pr = spotrebic(napeti, proud)
            print('----------------------------')
            print('příkon:', pr.prikon())
            print('odpor:', pr.odpor())
            print('----------------------------')
            print('Jestli chceš program ukončit tak zadej q/Q.')
            print('----------------------------')
        except ValueError:
            print('Chybné zadáni, zadejte znovu ! ')
            print('----------------------------')
            continue
        except ZeroDivisionError:
            print('V zadání je 0, nelze dělit nulou !')
            print('----------------------------')
            return
    print('\nKonec programu, děkuju za použití !')

if __name__ == '__main__':
    main()