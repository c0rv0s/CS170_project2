import sys
import matplotlib as plt
import pandas as pd

large = "CS170_LARGEtestdata/"
small = "CS170_SMALLtestdata/"

def leave_one_out_cross_validation(data, current_set, feature_to_add):
    df = pd.read_csv(small+data, delimiter= '\s+', index_col=False)
    return 1
    #print(df.loc[0][1])

def feature_search(data):
    df = pd.read_csv(small+data, delimiter= '\s+', index_col=False)
    current_features = []
    for i in range(1,len(df.columns)):
        print("on the "+str(i)+"th level of the search tree")
        feature_to_add = []
        best_accuracy_so_far = accuracy = 0
        for k in range(1,len(df.columns)):
            if k not in current_features:
                print("considering adding "+str(k)+"th feature")
                accuracy = leave_one_out_cross_validation(data,current_features,k)
            if accuracy > best_accuracy_so_far:
                best_accuracy_so_far = accuracy
                feature_to_add = [k]
        
        current_features += feature_to_add
        print("on level "+str(i)+" added feature "+str(feature_to_add)+" to current set")

#run the program, collect user input
def main():
    print("Welcome to Nathan Mueller's Feature Selection Algorithm.")
    data_choice = input("Type in the name of the file to test : \n")
    algo_choice = input("""Type the number of the algorithm you want to run.\n 
  1. Forward Selection\n  2. Backward Elimination\n  3. Nathan's Special Algorithm\n""")
    if algo_choice not in ["1","2","3"]:
        print("error: bad input")
        return
    
    feature_search(data_choice)

if __name__== "__main__":
    main()