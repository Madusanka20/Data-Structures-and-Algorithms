// Every node has 3 data ---> Data , next, previous
/*In C++, a struct (short for structure)is a user-defined data type that allows you to group different data types under a single name.
It is similar to a class, but with the key difference that by default,all members of a struct are public,whereas in a class, they are private by default.
A struct can contain variables (often called members or fields) ofvarious data types, including primitive types (like int, float, char),arrays,and other structs or classes.
It is a way to model and represent complex data by combining different types into a single entity.*/

#include<stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node* next;
    struct Node* prev;
};
struct Node* head; //global variable -pointer to head node

// void InsertAtHead(int x){
//     struct Node myNode; //Local variable , will be cleared from memory when function call will finish
//     myNode.data=x;
//     myNode.prev=NULL;
//     myNode.next=NULL;
// }

void InsertATHead(int x){
    struct Node* newNode =(struct Node*)malloc(sizeof(struct Node));
    newNode->data=x;
    newNode->prev=NULL;
    newNode->next=NULL;

}

int main(){

}

