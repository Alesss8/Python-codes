from prikon_c import spotrebic


def main():
    print('*---------------------------------------------*')
    print('Program vytvořil Aleš Toman IT4, dne 16.11.2023')
    print('*---------------------------------------------*')
    print('----------------------------')
    print('Jestli chceš program ukončit tak zadej q/Q.')
    print('----------------------------')
    while True:
        try:
            vstup = input('zadej napětí(U):')
            if vstup.upper() == 'Q':
                break
            napeti = float(vstup)

            vstup = input('zadej proud(I):')
            if vstup.upper() == 'Q':
                break
            proud = float(vstup)

            pr = spotrebic(napeti, proud)
            print('----------------------------')
            print('příkon:', pr.prikon())
            print('odpor:', pr.odpor())
            print('Jestli chceš program ukončit tak zadej q/Q.')
            print('----------------------------')
        except ValueError:
            print('Chybné zadání, zadejte znovu ! ')
            print('----------------------------')
            continue
        except ZeroDivisionError:
            print('V zadání je 0, nelze dělit nulou !')
            print('----------------------------')
            return
        except Exception as e:
            print(f'Nastala chyba: {e}')
            print('----------------------------')
            continue


if __name__ == '__main__':
    main()
