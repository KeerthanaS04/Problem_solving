#include<bits/stdc++.h>
using namespace std;

class Solution{
public: 
    bool isNStraightHand(vector<int>& hand,int groupSize){
        //Create a map to count the frequency of each card
        unordered_map<int,int> cardCounts;
        for(int card:hand){
            ++cardCounts[card]; //Increment the count for each card
        }
        //Sort the hand to arrange the cards in ascending order
        sort(hand.begin(),hand.end());
        //Traverse through the sorted hand
        for(int card:hand){
            //If the current card is still in count map(i.e, needed to form a group)
            if(cardCounts.count(card)){
                //Attempt to create a group starting with the current card
                for(int nextCard=card;nextCard<card+groupSize;nextCard++){
                    //If the next card in the sequence is missing, can't form a group
                    if(!cardCounts.count(nextCard)){
                        return false;
                    }
                    //Decrement count for the current card in the sequence
                    if(--cardCounts[nextCard]==0){
                        cardCounts.erase(nextCard); //Remove the card from the count map if count reaches zero
                    }
                }
            }
        }
        //If all the cards can be grouped, return true
        return true;
    }
};