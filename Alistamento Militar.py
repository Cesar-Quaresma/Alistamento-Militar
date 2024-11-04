from datetime import date
nome = str(input("Nome: "))
hoje = date.today().year
nasci = int(input("Ano de Nascimento: "))
idade = hoje - nasci
if idade == 18:
    print(f'\033[1:37m  O {nome} nasceu em {nasci}, cujo têm {idade} anos, e precisará comparecer à uma Junta de Serviço Militar para obter \033[1:31mdispensa\033[1:37m ou \033[1:31mnão.\033[1:37m')
elif idade > 18 :
    alistar = str(input("\033[1:37mVocê já compareceu à Junta de Serviços Militar? ")).upper()
    governo = str(input("Você Serviu o governo? S/N ")).upper()
    print(f'\033[1:37mO \033[1:39m{nome}\033[1:37m nasceu em \033[1:39m{nasci}\033[1:37m, com \033[1:39midade \033[1:37mde \033[1:39m{idade} anos\033[1:37m.\033[1:39m')
    if alistar in 'Ss' :
        print(f'S/N: {alistar}.Sua idade é de {idade}. Tudo Bêm {nome}. \033[1:34mVocê está isento de penalidade(s). Obrigado.\033[1:37m')
        if governo in 'Ss':
          print(f'S/N: {governo}. \033[1:32m Obrigado tambêm, por ter servido o governo. É uma honra tê-lo como cidadão da nossa pátria! Está dispensado. ')
        elif governo in 'Nn':
            print(f'S/N: {governo}.Você Não serviu o governo.')
    elif alistar in 'Nn':
        print(f'\033[1;31mNão houve \033[1:37mno caso, o comparecimento à Junta de Serviço Militar, bem como a de Alistamento Militar no tempo estimado.')
        print(f'Em nome de \033[1:34m{nome}\033[1:37m, as consequências se pesarão da seguinte forma: ')
        print("A - Sanção de \033[1:31mMulta\033[1:37m, por meio de instituição bancária conveniada com o Ministério da Defesa ou nos Correios. Porém, se \033[1:31mnão \npagamento da multa\033[1:37m: \nA-a - \033[1:31mNão\033[1:37m poderá requerer a \033[1:31mobtenção de passaporte\033[1:37m; \nA-b - \033[1:31mNão poderá\033[1:37m nesses termos, \033[1:31mobter matricula(s)\033[1:37m de universidades; \nA-c - Arcará tambêm com a \033[1:31mimpossibilidade de ingressar \033[1:37mcomo \033[1:31mfuncionário\033[1:37m, \033[1:31mempregado\033[1:37m, ou \033[1:31massociado à instituições\033[1:37m, \033[1:31m\nempresas\033[1:37m, ou \033[1:31massociação oficial\033[1:37m;")
        print("B - \033[1:31mPrecisará \033[1:37mcomparecer à \033[1:39mJunta Militar no Espaço Cidadão (Avenida São Paulo, 1550, Centro, terceiro andar. \nTambém de carater obrigatório, \033[1:31mlevar\033[1:37m: \033[1:31mRG\033[1:39m, \033[1:31mCPF\033[1:39m, \033[1:31mcomprovante de residência\033[1:39m,\033[1:31m declaração de escolaridade\033[1:39m, \ne \033[1:31mcertidão de nascimento\033[1:39m.")
elif idade < 18 :
    print(f"\033[1:39mSua idade é de {idade}. \033[1:35mAinda vai se alistar!")
print("FIM.")


