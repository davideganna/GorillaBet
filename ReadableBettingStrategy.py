from Squadra import Squadra
from Enumerators import *
from Partita import Partita 

class ReadableBettingStrategy:
    @staticmethod
    def CalculateStats(squadre:list[Squadra]):
        sq: Squadra
        p: Partita
        GoalFattiCasa: int
        GoalFattiTrans: int
        GoalSubitiCasa: int
        GoalSubitiTrans: int
        CoefficenteAttacco: float
        CoefficenteDifesa: float
        for sq in squadre:
            GoalFattiCasa = sq.GetGoalFattiInCasa()
            GoalFattiTrans = sq.GetGoalFattiAway()
            GoalSubitiCasa = sq.GetGoalSubitiInCasa()
            GoalSubitiTrans = sq.GetGoalSubitiAway()
            CoefficenteAttacco = sq.GetCoefficenteAttacco()
            CoefficenteDifesa = sq.GetCoefficenteDifesa()
            print(sq.Nome + " | " + str(CoefficenteAttacco) + " - "+ str(CoefficenteDifesa))

