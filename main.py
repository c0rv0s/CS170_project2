import sys
import pandas as pd
import math

large = "CS170_LARGEtestdata/"
small = "CS170_SMALLtestdata/"

def leave_one_out_cross_validation(data, current_features, feature_to_add=-1, feature_to_remove=-1, algo=False, best_accuracy_so_far=0):
    df = pd.read_csv(data, delimiter= '\s+', index_col=False, header=None)
    correct = 0
    features = current_features[:]
    if feature_to_add > -1:
        features.append(feature_to_add)
    if feature_to_remove > -1:
        features.remove(feature_to_remove)

    for index, row in df.iterrows():
        closest_dist = math.inf
        closest_index = 0
        for index2, row2 in df.iterrows():
            if index != index2:
                distance = 0
                for col in features:
                    distance += (row2.loc[col] - row.loc[col])**2
                if distance < closest_dist:
                    closest_dist = distance
                    closest_index = index2
        if df.loc[index][0] == df.loc[closest_index][0]:
            correct += 1
        if algo:
            if (len(df.index) - index + correct) < best_accuracy_so_far:
                print("low accuracy, terminating early", correct)
                return correct 
                
    print("accuracy", correct)
    return correct 

def forward_feature_search(data, algo=False):
    df = pd.read_csv(data, delimiter= '\s+', index_col=False, header=None)
    current_features = []
    best_accuracy_so_far = 0
    for i in range(1,len(df.columns)):
        print("on the "+str(i)+"th level of the search tree")
        feature_to_add = -1
        for k in range(1,len(df.columns)):
            if k not in current_features:
                print("considering adding "+str(k)+"th feature")
                if algo:
                    accuracy = leave_one_out_cross_validation(data,current_features, feature_to_add=k, algo=True, best_accuracy_so_far=best_accuracy_so_far)
                else:
                    accuracy = leave_one_out_cross_validation(data,current_features, feature_to_add=k)
                if accuracy > best_accuracy_so_far:
                    best_accuracy_so_far = accuracy
                    feature_to_add = k
        print("best so far: ",best_accuracy_so_far)
        if feature_to_add > -1:
            current_features.append(feature_to_add)
            print("on level "+str(i)+" added feature "+str(feature_to_add)+" to current set")
        else:
            print("nothing added to current set", current_features)
            return

    print(current_features)

def backward_feature_search(data):
    df = pd.read_csv(data, delimiter= '\s+', index_col=False, header=None)
    current_features = list(range(1, len(df.columns)))
    worst_accuracy_so_far = accuracy = math.inf
    for i in range(1,len(df.columns)):
        print("on the "+str(i)+"th level of the search tree")
        feature_to_remove = -1
        for k in range(1,len(df.columns)):
            if k in current_features:
                print("considering removing "+str(k)+"th feature")
                accuracy = leave_one_out_cross_validation(data,current_features,feature_to_remove=k)
                if accuracy < worst_accuracy_so_far:
                    worst_accuracy_so_far = accuracy
                    feature_to_remove = k
        print("worst so far: ",worst_accuracy_so_far)
        if feature_to_remove > -1:
            current_features.remove(feature_to_remove)
            print("on level "+str(i)+" removed feature "+str(feature_to_remove)+" from current set")
        else:
            print("nothing removed from current set")
    print(current_features)

#run the program, collect user input
def main():
    print("Welcome to Nathan Mueller's Feature Selection Algorithm.")
    #get file name 
    data_choice = input("Type in the name of the file to test : \n")
    #make full path from file name
    if data_choice[6] == "L":
        data_choice = large + data_choice
    else:
        data_choice = small+data_choice
    #get algorithm choice
    algo_choice = input("""Type the number of the algorithm you want to run.\n 
  1. Forward Selection\n  2. Backward Elimination\n  3. Nathan's Special Algorithm\n""")
    if algo_choice not in ["1","2","3"]:
        print("error: bad input")
        return
    if algo_choice == "1":
        forward_feature_search(data_choice)
    elif algo_choice == "2":
        backward_feature_search(data_choice)
    elif algo_choice == "3":
        forward_feature_search(data_choice, True)

if __name__== "__main__":
    main()