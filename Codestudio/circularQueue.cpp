#include<bits/stdc++.h>
#include<queue>
using namespace std;

class CircularQueue{
    int* arr;
    int front;
    int rear;
    int size;
    public:
    //Initialize your data structure

    CircularQueue(int n){
        size=n;
        arr=new int[size];
        front=rear=-1;
    }

    //Enqueues 'X' into the queue. Returns true if it gets pushed into the stack, and false otherwise
    bool enqueue(int value){
        //to check whether the queue is full or not
        if((front==0 && rear=size-1)||(rear==(front-1)%(size-1))){
            // cout<<"Queue is full";
            return false;
        }else if(front==-1){//first element to push
            front=rear=0;
        }else if(rear==size-1 && front!=0){
            rear=0; //to maintain cyclic nature
        }else{
            rear++;
        }
        //push inside the queue
        arr[rear]=value;
        return value;
    }

    //Dequeues top element from queue. Returns -1 if stack is empty, otherwise return the popped element
    int dequeue(){
        if(front==-1){ //to check queue is empty
            return -1;
        }
        int ans=arr[front];
        arr[front]=-1;

        if(front==rear){ //single element is present
            front=rear=-1;
        }else if(front==size-1){ //to maintain cyclic nature
            front=0;
        }else{//normal flow
            front++;
        }
        return ans;
    }
};