public class bubbleSort {
    
    public int[] sorting(int array[]){

        int temp = 0;

        for (int swi=0; swi<array.length-1;swi++){
            for (int swj = 0; swj < array.length-swi-1;swj++){
                if(array[swj] > array[swj+1]){
                    temp = array[swj];
                    array[swj] = array[swj+1];
                    array[swj+1] = temp;
                }
            }
        }
        return array;
    }

    public static void main(String[] args){
    int[] array = {12, 3, 9, 32, 4, 56, 0, 1, 2 };

    bubbleSort obj = new bubbleSort();

    array = obj.sorting(array);
    System.out.print("Sorted Array: ");
    for(int swi=0;swi<array.length;swi++){
        System.out.print(array[swi] + " ");
    }
    }
}

// Simple Bubble Sort Problem in Java- Without any optimization