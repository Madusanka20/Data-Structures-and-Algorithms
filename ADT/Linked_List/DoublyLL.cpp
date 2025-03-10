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

// Function to create a new node
struct Node* GetNewNode(int x) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = x;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

// Insert at the head of the list
void InsertAtHead(int x) {
    struct Node* newNode = GetNewNode(x);
    if (head == NULL) {
        head = newNode;
        return;
    }
    head->prev = newNode;
    newNode->next = head;
    head = newNode;
}

// Insert at a given position (1-based index)
void InsertAtPosition(int x, int position) {
    struct Node* newNode = GetNewNode(x);
    if (position == 1) {  // If inserting at head
        InsertAtHead(x);
        return;
    }

    struct Node* temp = head;
    for (int i = 1; temp != NULL && i < position - 1; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {  // Position is beyond the last node
        printf("Invalid position!\n");
        return;
    }

    newNode->next = temp->next;
    newNode->prev = temp;

    if (temp->next != NULL) {
        temp->next->prev = newNode;
    }

    temp->next = newNode;
}

// Delete a node at a given position (1-based index)
void DeleteNode(int position) {
    if (head == NULL) return;  // Empty list case

    struct Node* temp = head;

    if (position == 1) {  // If deleting head node
        head = head->next;
        if (head != NULL) head->prev = NULL;
        free(temp);
        return;
    }

    for (int i = 1; temp != NULL && i < position; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {  // Position beyond list length
        printf("Invalid position!\n");
        return;
    }

    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    }

    if (temp->prev != NULL) {
        temp->prev->next = temp->next;
    }

    free(temp);
}

// Print list forward
void PrintForward() {
    struct Node* temp = head;
    printf("Forward: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// Print list in reverse
void PrintReverse() {
    struct Node* temp = head;
    if (temp == NULL) return;

    while (temp->next != NULL) {  // Move to the last node
        temp = temp->next;
    }

    printf("Reverse: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->prev;
    }
    printf("\n");
}

// Main function
int main() {
    InsertAtHead(5);
    InsertAtHead(10);
    InsertAtHead(15);
    InsertAtHead(20);

    printf("Initial List:\n");
    PrintForward();
    PrintReverse();

    InsertAtPosition(25, 2);  // Insert 25 at position 2
    printf("\nAfter inserting 25 at position 2:\n");
    PrintForward();

    DeleteNode(3);  // Delete node at position 3
    printf("\nAfter deleting node at position 3:\n");
    PrintForward();
    PrintReverse();

    return 0;
}