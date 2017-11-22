# Practice understanding the selections sort

source = [4,2,1,10,5,3,100]
# Big O = n^2

for i in range(len(source)):
    mini = min(source[i:])             #find minimum element
    min_index = source[i:].index(mini) #find index of minimum element
    source[i + min_index] = source[i] #replace element at min_index with first element
    source[i] = mini                  #replace first element with min element
print (source)



array = [1,45,10,35,100,13,147,500,80]
size = len(array)


for i in range(0,size):                # loops through the entire array based on its size
    for j in range(i+1,size):          # moves past the first element
        if array[j] < array[i]:        # checks to see if its min element
            min = array[j];            # sets minimum element
            array[j] = array[i];       # moves the first element to the min location
            array[i] = min;            # moves the min element to the first location

print(array)
