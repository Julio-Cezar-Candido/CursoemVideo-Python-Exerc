peso = float(input('Qual é o seu peso em? (Kg) '))
altura = float(input('E qual é a sua altura? (m) '))
imc = peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é igual a {:.2f}, você está abaixo do seu peso ideal!!!'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é igual a {:.2f}, você está no seu peso ideal.'.format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é igual a {:.2f}, você está com sobrepeso!!!'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é igual a {:.2f}, você está com obesidade!!!!!!'.format(imc))
elif imc > 40:
    print('Seu IMC é igual a {:.2f}, você está com OBESIDADE MÓRBITA!!!! CUIDE-SE'.format(imc))
