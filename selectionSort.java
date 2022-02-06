public class selectionSort{

    public int[] sorting(int array[]){

        int len = array.length;
        for (int swi = 0; swi < len-1; swi++)
        {
            int min_index = swi;
            for (int swj = swi+1; swj < len; swj++)
                if (array[swj] < array[min_index])
                    min_index = swj;
  
            int temp = array[min_index];
            array[min_index] = array[swi];
            array[swi] = temp;
        }

        return array;
    }

    public static void main(String[] args) {

    int[] array = {12, 3, 9, 32, 4, 56, 0, 1, 2};
    

    selectionSort obj = new selectionSort();

    array = obj.sorting(array);
    System.out.print("Sorted Array: ");
    for(int swi=0;swi<array.length;swi++){
        System.out.print(array[swi] + " ");
    }
        
    }
}