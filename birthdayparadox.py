import datetime
import random


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
          "You can find out more about the Birthday Paradox at\n"
          "https://en.wikipedia.or/wiki/Birthday_problem.")

    while True:
        print("How many people shall we generate with random birthdays?")
        bd_num = 0
        while bd_num < 2:
            bd_num = input('> ')
            bd_num = int(bd_num)
            if bd_num < 2:
                print("Value must be 2 or greater...")

        a = 1
        same = 0
        while a <= 100000:
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            bdays = []

            # Creating random birthdays
            for i in range(bd_num):
                bday = ''
                # Shuffling the list of months and adding the first one in the list
                random.shuffle(months)
                bday += months[0]

                # If month is feb, days will be limited to 28 else, we will use a full range to 31 for now
                # TODO: separate months that have 30 days and months with 31 days
                # TODO: add years to calculate if february is a leap year
                if bday == 'Feb':
                    days = list(range(1, 29))
                else:
                    days = list(range(1, 32))

                random.shuffle(days)
                bday += ' '
                bday += str(days[0])

                bdays.append(bday)

            # print("==== Simulation {} bdays ====".format(a))
            # print(bdays)

            for k in bdays:
                # print("\t-- Bday: {} --".format(k))
                for l in bdays[bdays.index(k)+1:]:
                    # print("check: {}".format(l))
                    if k == l:
                        # print("\t** MATCH **")
                        same += 1
                        a += 1
                        bdays.pop(bdays.index(k))
                        break
            # print("Same bdays: {}".format(same))
            a += 1

        percent = same/100000
        percent *= 100

        print("{} % chance of two people having the same birthday in a group of {} people\n"
              "after running 100000 simulations".format(percent, bd_num))

        print("Would you like to run another test(y/n)?")
        user = input('> ')
        if user == 'y' or user == 'Y':
            continue
        elif user == 'n' or user == 'N':
            break
        else:
            print("Invalid input. Exiting program....")
            break

    return 0


if __name__ == '__main__':
    main()