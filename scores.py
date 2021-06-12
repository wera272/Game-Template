from blocks import *
def update_score(nscore):
    #score = max_score()

    with open('scores.txt', 'r') as f:
        file = f.readlines()  # reads all the lines in as a list
        #last = int(file[0])  # gets the first line of the file
        f = open('scores.txt', 'r')  # opens the file in read mode
        file = f.readlines()  # reads all the lines in as a list
        first = int(file[0])  # gets the first line of the file
        second = int(file[1])
        third = int(file[2])
        score_list = [first, second, third]
        for i in range(len(file)):

            if first < int(nscore):  # sees if the current score is greater than the previous best
                f.close()  # closes/saves the file
                file = open('scores.txt', 'w')  # reopens it in write mode
                file.write(str(nscore) + '\n')
                file.write(str(first) + '\n')
                file.write(str(second))

                # writes the best score
                file.close()  # closes/saves the file

                return nscore
            elif second < int(nscore):
                f.close()  # closes/saves the file
                file = open('scores.txt', 'w')  # reopens it in write mode
                file.write(str(first) + '\n')
                file.write(str(nscore) + '\n')
                file.write(str(second))
                # writes the best score
                file.close()  # closes/saves the file
                return nscore
            elif third < int(nscore):
                f.close()  # closes/saves the file
                file = open('scores.txt', 'w')  # reopens it in write mode
                file.write(str(first) + '\n')
                file.write(str(second) + '\n')
                file.write(str(nscore))
                # writes the best score
                file.close()  # closes/saves the file
                return nscore
            else:
                f.close()  # closes/saves the file
                file = open('scores.txt', 'w')  # reopens it in write mode
                file.write(str(first) + '\n')  # writes the best score
                file.write(str(second) + '\n')
                file.write(str(third) + '\n')
                file.close()  # closes/saves the file

                return nscore

            return third

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score


