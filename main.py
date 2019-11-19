import sys
import matplotlib as plt
import pandas as pd

large = "CS170_LARGEtestdata/"
small = "CS170_SMALLtestdata/"

def nn(data):
    df = pd.read_csv(small+data, delimiter= '\s+', index_col=False)
    #print(df.loc[0][1])


#run the program, collect user input
def main():
    print("Welcome to Nathan Mueller's Feature Selection Algorithm.")

    data_choice = input("Type in the name of the file to test : \n")
    algo_choice = input("Type the number of the algorithm you want to run.\n  1. Forward Selection\n  2. Backward Elimination\n  3. Nathan's Special Algorithm\n")
    if algo_choice not in ["1","2","3"]:
        print("error: bad input")
        return
    
    nn(data_choice)
    

if __name__== "__main__":
    main()