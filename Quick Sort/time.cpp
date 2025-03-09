#include <iostream>
#include <vector>
#include <stack>
#include <chrono>
#include <cstdlib>

using namespace std;
using namespace chrono;

// Function to partition the array (used by both recursive and iterative quicksort)
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Recursive Quick Sort
void quickSortRecursive(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortRecursive(arr, low, pi - 1);
        quickSortRecursive(arr, pi + 1, high);
    }
}

// Iterative Quick Sort
void quickSortIterative(vector<int>& arr) {
    int n = arr.size();
    if (n <= 1) return;

    stack<int> s;
    s.push(0);
    s.push(n - 1);

    while (!s.empty()) {
        int high = s.top(); s.pop();
        int low = s.top(); s.pop();

        int pi = partition(arr, low, high);

        if (pi - 1 > low) {
            s.push(low);
            s.push(pi - 1);
        }
        if (pi + 1 < high) {
            s.push(pi + 1);
            s.push(high);
        }
    }
}

// Function to generate random numbers
vector<int> generateRandomArray(int size) {
    vector<int> arr(size);
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100000;
    }
    return arr;
}

// Main function to compare execution times
int main() {
    vector<int> sizes = {1000, 5000, 10000, 50000, 100000}; // Different input sizes
    cout << "Size\tRecursive (ms)\tIterative (ms)\n";

    for (int size : sizes) {
        vector<int> arr1 = generateRandomArray(size);
        vector<int> arr2 = arr1; // Copy for iterative sort

        auto start1 = high_resolution_clock::now();
        quickSortRecursive(arr1, 0, size - 1);
        auto end1 = high_resolution_clock::now();
        double time1 = duration<double, milli>(end1 - start1).count();

        auto start2 = high_resolution_clock::now();
        quickSortIterative(arr2);
        auto end2 = high_resolution_clock::now();
        double time2 = duration<double, milli>(end2 - start2).count();

        cout << size << "\t" << time1 << "\t\t" << time2 << "\n";
    }

    return 0;
}
