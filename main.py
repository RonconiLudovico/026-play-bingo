from random import randint, shuffle


def bingo_card():
    bingoCard = {}
    B = []
    I = []
    N = []
    G = []
    O = []

    # Here we loop until there are 5 elements in each letter list to add a random int, making
    # sure not to add same numbers to the lists. After the loop we add the lists to the dict
    # using each letter as Key
    while len(B) < 5:
        num = randint(1, 15)
        B.append(num) if num not in B else B.remove(num)
    bingoCard["b"] = B

    while len(I) < 5:
        num = randint(16, 30)
        I.append(num) if num not in I else I.remove(num)
    bingoCard["i"] = I

    while len(N) < 5:
        num = randint(31, 45)
        N.append(num) if num not in N else N.remove(num)
    bingoCard["n"] = N

    while len(G) < 5:
        num = randint(46, 60)
        G.append(num) if num not in G else G.remove(num)
    bingoCard["g"] = G

    while len(O) < 5:
        num = randint(61, 75)
        O.append(num) if num not in O else O.remove(num)
    bingoCard["o"] = O

    # finally we return the dictionary
    return bingoCard


# Here we create a list with all the bingo calls and then shuffle them before returning them
def bingo_call():
    bingoCalls = []

    for i in range(1, 76):
        if i < 16:
            bingoCalls.append("b" + str(i))
        elif 15 < i < 31:
            bingoCalls.append("i" + str(i))
        elif 30 < i < 46:
            bingoCalls.append("n" + str(i))
        elif 45 < i < 61:
            bingoCalls.append("g" + str(i))
        elif 60 < i < 76:
            bingoCalls.append("o" + str(i))

    shuffle(bingoCalls)

    return bingoCalls


# The following function works by starting a count at 0, then it iterates through every element of bingo_call(), defining columns and numbers by splicing the elements
# then checks if the number called by the iteration is in the card and if so, it updates the number to 0
# each of these cycles increases the count by 1
# Then if the given winning conditions are met, the for loop is stopped and the count is returned
def play_games():
    count = 0
    card = bingo_card()

    for call in bingo_call():
        column = call[0]
        number = int(call[1:])

        if number in card[column]:
            card[column][card[column].index(number)] = 0
        count += 1
        # Here we state the winning conditions
        if (
            card["b"] == [0, 0, 0, 0, 0]
            or card["i"] == [0, 0, 0, 0, 0]
            or card["n"] == [0, 0, 0, 0, 0]
            or card["g"] == [0, 0, 0, 0, 0]
            or card["o"] == [0, 0, 0, 0, 0]
        ):
            break
        elif (
            card["b"][0] == 0
            and card["i"][1] == 0
            and card["n"][2] == 0
            and card["g"][3] == 0
            and card["o"][4] == 0
        ):
            break
        elif (
            card["b"][4] == 0
            and card["i"][3] == 0
            and card["n"][2] == 0
            and card["g"][1] == 0
            and card["o"][0] == 0
        ):
            break
        elif (
            card["b"][0] == 0
            and card["i"][0] == 0
            and card["n"][0] == 0
            and card["g"][0] == 0
            and card["o"][0] == 0
        ):
            break
        elif (
            card["b"][1] == 0
            and card["i"][1] == 0
            and card["n"][1] == 0
            and card["g"][1] == 0
            and card["o"][1] == 0
        ):
            break
        elif (
            card["b"][2] == 0
            and card["i"][2] == 0
            and card["n"][2] == 0
            and card["g"][2] == 0
            and card["o"][2] == 0
        ):
            break
        elif (
            card["b"][3] == 0
            and card["i"][3] == 0
            and card["n"][3] == 0
            and card["g"][3] == 0
            and card["o"][3] == 0
        ):
            break
        elif (
            card["b"][4] == 0
            and card["i"][4] == 0
            and card["n"][4] == 0
            and card["g"][4] == 0
            and card["o"][4] == 0
        ):
            break

    return count


# Finally in the main function we state different variables, number of games(to loop 1000 games), an empty list in which to store all the counts of rounds needed to win
# a minimum variable being 75 as the extreme would be 75 rounds minimum to win, a maximum being 0 which will be increased if an higher number is found
# and finally an average in which we will store the sum of all the values to later divide by 1000
# finally we return an f-string stating all these updated variables
def main():
    n_games = 0
    rounds_to_win = []
    minimum = 75
    maximum = 0
    average = 0

    while n_games < 1000:
        rounds_to_win.append(play_games())
        n_games += 1

    for i in rounds_to_win:
        if i < minimum:
            minimum = i

        if i > maximum:
            maximum = i

        average += i

    return f"Minimum: {minimum} \nMaximum: {maximum} \nAverage: {average / 1000}"


if __name__ == "__main__":
    print(main())
