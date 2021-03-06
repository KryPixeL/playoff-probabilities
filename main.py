import math

while True:
    try:
        p = float(input("\nProbability of better team winning a game: "))

        if 0.5 > p or p > 1:
            raise Exception("value not in range")

        g = int(input("\nNumber of games in the playoff: "))

        if g <= 0:
            raise Exception("value less than or 0")

        if g % 2 == 0:
            raise Exception("value is not odd")

        g = math.ceil(g / 2)
        f = g - 1

        terms = []
        betterTeamResult = 0

        for c in range(0, g):
            terms.append(math.comb((f + c), f) * p**g * (1 - p)**(f - f + c))

        for i in terms:
            betterTeamResult += i

        worseTeamResult = 1 - betterTeamResult

        print("\nOdds of better team winning playoffs:", betterTeamResult)
        print("Odds of worse team winning playoffs: ", worseTeamResult)
        print("--------------------------------------------------------")

    except Exception as e:
        print(e)
