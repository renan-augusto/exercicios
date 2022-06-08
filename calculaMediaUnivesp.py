print("Bem vindo ao cálculo da nota necessária da UNIVESP")
n1 = eval(input("Qual a sua nota final das atividades avaliativas?\n"))

n2 = (5 - n1*0.4)/0.60
materia = input("Qual o nome da sua matéria?\n")
print(f"Você precisa de {n2} na prova na disciplina de {materia}.")