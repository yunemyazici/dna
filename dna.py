import csv
import sys


def main():
    if len(sys.argv)!=3:
        print("Usage: dna.py database sequence")
        sys.exit(1)

    database = []
    with open(sys.argv[1],"r") as database_file:
        reader = csv.DictReader(database_file)
        for row in reader:
            database.append(row)
    sub = database[0].keys()
    subsequences = []
    for i in sub:
        if i != "name":
            subsequences.append(i)


    sequence=[]

    with open(sys.argv[2],"r") as s:
        reader1 = csv.reader(s)
        for char in reader1:
            sequence = char

    final_results = {}

    for each_subsequence in range(len(subsequences)):
        result = longest_match(sequence[0],subsequences[each_subsequence])
        final_results[subsequences[each_subsequence]]=result



    person = None


    for i in range(len(database)):
        point = 0
        for j in subsequences:
            if(int(database[i][j])==final_results[j]):
                point+=1
        if point == len(subsequences):
            person = database[i]['name']
            break



    if person != None:
        print(f"The person is {person}")
    else:
        print("No match")
    return



def longest_match(sequence, subsequence):
    count = 0
    run = 0
    length = len(subsequence)
    i = 0
    while(i<len(sequence)):
        if sequence[i:(i+length)]==subsequence:
            run += 1
            i += length
        else:
            if run > count:
                count = run
            run = 0
            i += 1

    return count


main()
