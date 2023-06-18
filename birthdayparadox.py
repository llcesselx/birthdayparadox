import datetime, random


def main():
    print("The Birthday Paradox, also called the Birthday Problem, is\n"
          "the surprisingly high probability that two people will have\n"
          "the same birthday even in a small group of people. In a group\n"
          "of 70 people, theres a 99.99 percent chance of two people\n"
          "having a matching birthday. BUt even in a group as small as\n"
          "23 people, there's a 50 percent chance of matching a birthday.\n"
          "This program performs several probability experiments to determine\n"
          "the percentages for groups of different sizes. We call these\n"
          "types of experiments, in which we conduct multiple random trials\n"
          "to understand the likely outcomes, Monte Carlo experiments.\n"
          "\n"
          "You can find out more about the Birthday Paradox at 'https://en.\n"
          "wikipedia.or/wiki/Birthday_problem'.")

    print("How many people shall we generate with random birthdays?")
    bd_num = 0
    while bd_num < 2:
        bd_num = input('> ')
        bd_num = int(bd_num)
        if bd_num < 2:
            print("Value must be 2 or greater...")

    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    days = ()
    bdays = ()

    for i in range(bd_num):
        random.shuffle(months)

    return 0