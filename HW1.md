First, I use the sample code to import my data "108061101.csv".  
Then I use data.append() to grab the data into the list, and scan the the station list of 5 target station on the problem.  
Later, I delete the -99.000 and -999.000 pressure data in each station by "if" statement, and store the new data into the "target_data" list.  
Finally, I can add all the data together and find their average by two for loops, since the "target_data" list is two-dimension (i index for station id, j index for pressure data).  
I also add one statement two find if all data are -99.000 and -999.000, which means the length of the list (target_data[i]) is zero, so we have to output "None".  
Following is my output result:  
[['C0A880', 1018.66], ['C0F9A0', 968.52], ['C0G640', 1018.41], ['C0R190', 1012.15], ['C0X260', 1013.19]]  

