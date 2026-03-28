# uso di un dizionario per memorizzare i voti di n materie

report = {}   # dizionario vuoto 
new_subject = 'Y'
while new_subject == 'Y':
    subject = input('type the name of the subject: ')
    report[subject] = []  # creo una nuova chiave e le associo una lista vuota
    new_vote = 'Y'

    while new_vote == 'Y':
        vote = float(input('type a vote: '))
        report[subject] = report[subject] + [float(vote)] # concateno il nuovo voto alla lista
        new_vote = input('do you want to add another vote? [Y/n]  ')

    new_subject = input('do you want to add another subject? [Y/n] ')

print(report)   # stampo la pagella

# operazioni sul dizionario

# media dei voti per ogni materia (una materia ha almeno 1 voto)
for subject in report:
    tot = 0
    for vote in report[subject]:
        tot += vote
    avg = tot/(len(report[subject]))
    print(f"{subject}: {avg}")

# percentuale di sufficienze per ogni materia
for subject in report:
    suff_counter = 0
    for vote in report[subject]:
        if vote > 5:
            suff_counter += 1
    suff_perc = suff_counter/len(report[subject])*100
    print(f"{subject}: {suff_perc}%")