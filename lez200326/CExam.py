# definizione e uso della classe CExam

class CExam:

    # metodo costruttore
    def __init__(self, name, first_vote, second_vote):
        self.name = name
        self.first_vote = first_vote
        self.second_vote = second_vote

    # stampa nome esame
    def print_name(self):
        print(self.name)

    # stampa voto finale
    def print_final_vote(self):
        print(self._calc_avg(self.first_vote, self.second_vote))

    # calcola media
    def _calc_avg(self, first_vote, second_vote):
        avg = (self.first_vote + self.second_vote)//2
        return avg

# creo degli oggetti della classe CExam
lpo = CExam("Linguaggi di programmazione orientati agli oggetti", int("25"), int("28"))
pweb = CExam("Programmazione WEB", int("29"), int("26"))

lpo.print_name()
lpo.print_final_vote()
pweb.print_name()
pweb.print_final_vote()
