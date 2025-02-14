// Insertion sorting 
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void insertionSort(vector<int>& arr){
    for(int i =1 ; i< arr.size();i++){
        int current_element=arr[i];
        int position=i;
        while(current_element<arr[position-1] && position>0){
            arr[position]=arr[position-1];
            position-=1;
        }
        arr[position]=current_element;
        for (int i = 0; i < arr.size(); i++) {  // Print the array in each iteration 
            cout << arr[i] << ' ';
            
        }
        cout<<endl;
    }
    cout << "Final_Sorted_Array : ";
    for (int i = 0; i < arr.size(); i++) {
        
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main (){
    vector<int> array={2,9,3,6,1,4};
    insertionSort(array);
    return 0;
}