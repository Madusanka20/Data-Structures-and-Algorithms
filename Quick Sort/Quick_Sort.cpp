//Quick Sort    
/*For this we need to get Pivot element 
  Generally we take right most or left  
  most element or random element as a
  pivot element. In First iteration we 
  take pivot in to it's actuall position.
  And this method use devide and conquor method .*/

  #include <iostream>
  #include <vector>
  
  using namespace std;
  
  int pivot_place(vector<int>& array, int first, int last) {
      int pivot = array[first]; // First element as pivot
      cout<<pivot<<endl;
      int left = first + 1;
      int right = last;
  
      while (true) {
          while (left <= right && array[left] <= pivot) left++;
          while (left <= right && array[right] >= pivot) right--;
  
          if (right < left) break;
          
          swap(array[left], array[right]);
          for (int num : array) {
            cout << num << ' ';
        }
        cout<<endl;

      }
  
      swap(array[first], array[right]); // Place pivot in correct position
      return right;
  }
  
  void quicksort(vector<int>& array, int first, int last) {
      if (first < last) {
          int p = pivot_place(array, first, last);
          quicksort(array, first, p - 1);
          quicksort(array, p + 1, last);
      }
  }
  
  int main() {
      vector<int> array = {2, 9, 3, 6, 1, 4,56,34,2,3,7};
      int length = array.size();
  
      quicksort(array, 0, length - 1);
  
      for (int num : array) {
          cout << num << ' ';
      }
      return 0;
  }
  