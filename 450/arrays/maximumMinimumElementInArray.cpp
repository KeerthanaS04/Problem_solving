#include<bits/stdc++.h>
using namespace std;

struct Pair{
    int max;
    int min;
};

// Approach-1 = Using Sorting

/* The time complexity of this approach is O(nlogn), where n is the number of elements in the array, as we are using
   a sorting algorithm. Ths space complexity is O(1), as we are not using any extra space 


Pair getMinMax(int arr[],int n){
    Pair minmax;

    sort(arr,arr+n);

    minmax.min=arr[0];
    minmax.max=arr[n-1];

    return minmax;
}
*/

// Approach-2 = Using Linear Search

/* Time Complexity: O(n)
   Auxiliary Space: O(1) as no extra space was needed. 
   In this method, the total number of comparisons is 1 + 2(n-2) in the worst case and 1 + n – 2 in the best case. 
   In the above implementation, the worst case occurs when elements are sorted in descending order and the best case
   occurs when elements are sorted in ascending order.
Pair getMinMax(int arr[],int n){
    struct Pair minmax;

    //If there is only one element then return it as both min and max
    if(n==1){
        minmax.max=arr[0];
        minmax.min=arr[0];
    }

    //If there is more than one element then initialize both min and max
    if(arr[0]>arr[1]){
        minmax.max=arr[0];
        minmax.min=arr[1];
    }else{
        minmax.max=arr[1];
        minmax.min=arr[0];
    }

    for(int i=2;i<n;i++){
        if(arr[i]>minmax.max){
            minmax.max=arr[i];
        }else if(arr[i]<minmax.min){
            minmax.min=arr[i];
        }
    }
    return minmax;
}

*/

// Approach-3 = Using tournament method

/* Time Complexity: O(n)
   Auxiliary space: O(logn) as the stack space will be filled for the maximum height of the tree formed during
   recursive calls same as binary tree

struct Pair getMinMax(int arr[],int low, int high){
    struct Pair minmax,mm1,mm2;
    int mid;

    //If there is only one element
    if(low==high){
        minmax.max=arr[low];
        minmax.min=arr[high];
        return minmax;
    }

    //If there is two element
    if(high==low+1){
        if(arr[low]>arr[high]){
            minmax.max=arr[low];
            minmax.min=arr[high];
        }else{
            minmax.max=arr[high];
            minmax.min=arr[low];
        }
        return minmax;
    }

    //If there are more than two elements
    mid=(high+low)/2;
    mm1=getMinMax(arr,low,mid);
    mm2=getMinMax(arr,mid+1,high);

    //compare two minimums of two parts
    if(mm1.min<mm2.min){
        minmax.min=mm1.min;
    }else{
        minmax.min=mm2.min;
    }

    //compare two maximums of two parts
    if(mm1.max<mm2.max){
        minmax.max=mm2.max;
    }else{
        minmax.max=mm1.max;
    }

    return minmax;
};
*/

//Approach-4: By comparing in pairs
struct Pair getMinMax(int arr[],int n){
    struct Pair minmax;
    int i;

    //If array has even number of elements then initialize the first two elements as minimum and maximum
    if(n%2==0){
        if(arr[0]>arr[1]){
            minmax.max=arr[0];
            minmax.min=arr[1];
        }else{
            minmax.max=arr[1];
            minmax.min=arr[0];  
        }
    //setting the starting index for loop
    i=2;
    }else{
        //If array has odd number of elements then initialize the first element as minimum and maximum
        minmax.max=arr[0];
        minmax.min=arr[0];

        //setting the starting index for loop
        i=1;
    }

    //In the while loop, pick elements in pair and compare the pair with max and min so far
    while(i<n-1){
        if(arr[i]>arr[i+1]){
            if(arr[i]>minmax.max)
                minmax.max=arr[i];
            if(arr[i+1]<minmax.min)
                minmax.min=arr[i+1];
        }else{
            if(arr[i+1]>minmax.max)
                minmax.max=arr[i+1];
            if(arr[i]<minmax.min)
                minmax.min=arr[i];
        }
        //Increase the element by 2 as two elements are processed in the loop
        i+=2;
    }
    return minmax;
}

int main(){
    int arr[]={1000,11,445,1,330,3000};
    int arr_size=sizeof(arr)/sizeof(arr[0]);

    Pair minmax=getMinMax(arr,arr_size);

    cout<<"Minimum element is "<<minmax.min<<endl;
    cout<<"Maximum element is "<<minmax.max<<endl;

    return 0;
}