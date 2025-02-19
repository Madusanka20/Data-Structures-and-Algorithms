#include <iostream>
#include <vector>

using namespace std;

// Bubble Sort Function( Not an optimised version)
void bubbleSort(vector<int>& array) {
    int n = array.size();
    
    for (int j = 0; j < n - 1; j++) {  // Outer loop for passes
        for (int i = 0; i < n  - 1; i++) {  // Inner loop for comparisons //For optimised version put n-j-1
            if (array[i] > array[i + 1]) {
                swap(array[i], array[i + 1]);  // Swap elements if needed
            }else{
                for (int num : array) {
                    cout << num << " ";
                }
                cout << endl;
            }
        }
    }
}

//Function to Print Array
void printArray(const vector<int>& array) {
    for (int num : array) {
        cout << num << " ";
    }
    cout << endl;
}

//Main Function
int main() {
    vector<int> array = {10, 2, 53, 12, 6};  // Input array

    cout << "Original array: ";
    printArray(array);

    bubbleSort(array);  // Call Bubble Sort Function

    cout << "Sorted array: ";
    printArray(array);

    return 0;
}
