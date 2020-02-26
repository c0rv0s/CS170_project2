# Feature Selection
Find the most relevant labels for predicting classes via nearest neighbor using forward and backward search. I also developed an optimized forward search with the same results but better run time.

## Comparison of Algorithms

The three algorithms used are Forward Search, Backward Search and then an improved algorithm I developed.

## Forward Search
Forward search starts with an empty set of features and tests adding new ones one by one. For each level of the search tree it finds the feature that will increase the accuracy the most and adds it to the current set. If no new features are added the algorithm terminates.
## Backward Search
Backward search is forward search in reverse. It starts with all the features and tests removing features one by one. The feature removal that improves accuracy the most is kept. The algorithm runs until there are no more accuracy improvements to be made.
Backward search runs longer than forward search because it is using more features during the cross validation step. During the first iteration forward search performs one distance calculation per row while the number of calculations backward search does is the number of features in the set. The larger the set, the greater the disparity.
## My Special Algorithm
My special algorithm is simply forward search with an added exit case: if the current iteration has more wrong predictions than the best case so far, it will terminate since it is impossible for this feature to be result in a better accuracy. This shaves a significant amount of time off the algorithm’s run time. It does not affect accuracy.

Datasets such as the Iris dataset from UC Irvine work excellently with this code.
