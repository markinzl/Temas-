data = input('Digite a data do nascimento do Marcus (dd/mm/aaaa ou dd/mm/aa): ')

if data == '14/08/2006' or data == '14/08/06' or data == '14082006' or data == '140806':
    print('Data validada corretamente!')
else:
    print('Data incorreta, tente novamente.')