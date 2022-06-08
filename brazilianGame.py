print("Bem-vindo ao jogo dos navegantes!")
print("""Você é um navagador da idade média e está prestes a desbravar os sete mares em busca de novas aventuras!     ~;
                  ,/|\,
                ,/' |\ \,
              ,/'   | |  \,
            ,/'     | |   |
          ,/'       |/    |
        ,/__________|-----' ,
       ___.....-----''-----/
 jgs   \                  /
   ~~-~^~^~`~^~`~^^~^~-^~^~^~-~^~^
     ~-^~^-`~^~-^~^`^~^-^~^`^~^-~^""")

coordinate = input("Começa a sua jornada e você tem que decidir para qual direção irá. Então? Qual será? Digite L para "
                   "leste, O para oeste ou S para sul\n").lower()

destiny = 0
if coordinate == "l":
    print("Uma sombra ameaçadora é observada no fundo do mar, seu navio foi atacado por um kraken é o fim - Game Over")
    print(''','""`.
            / _  _ \,
            |(@)(@)|
            )  __  (
           /,'))((`.\,
          (( ((  )) ))      
           `\ `)(' / ''')

elif coordinate == "o":
    destiny += 1
else:
    print("Seu navio foi atacado e afundado por corsários da coroa britânica - Game Over")
    print('''      
                    .-"_______"-.
                   /            .\.
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_)
          ''')

if destiny == 1:
    print("Você chegou a um paraíso tropical e atraca seu navio esse local será futuramente o Brasil!")
    print("Você descobriu o Brasil, parabéns!")
    print('''".''.
 (~~~~)
   ||
 __||__
/______\
  |  |' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
  |  |'|o| - - - - - - - - - - - - - - - - - - - - - - - - -||
  |  |'| |                                                  ||
  |  |'| |                      . ' .                       ||
  |  |'| |                  . '       ' .                   ||
  |  |'| |              . '    .-'"'-.    ' .               ||
  |  |'| |          . '      ,"       ".      ' .           ||
  |  |'| |      . '        /:           :\        ' .       ||
  |  |'| |  . '            ;  .          ;            ' .   ||
  |  |'| |    ' .          \: . .       :/          . '     ||
  |  |'| |        ' .        `. . .    ,/       . '         ||
  |  |'| |            ' .      `-.,,.-'     . '             ||
  |  |'| |                ' .           . '                 ||
  |  |'| |                    ' .   . '                     ||
  |  |'| |                        '                         ||
  |  |'|o|-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_||
  |  |'
  |  |'
  |  |'
  |  |'
  '~~'")''')