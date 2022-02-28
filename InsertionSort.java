public class InsertionSort {
    public static void main(String[] args){
        int[] array = {6,5,4,3,2,1};

        int[] result = sort(array);

        for (int swi = 0; swi < result.length;swi++){
            System.out.print(result[swi] + " ");
        }
    }

    public static int[] sort(int[] array){
        int swi, swj, key;

        for (swi=1; swi<array.length;swi++){
            swj = swi - 1;
            key = array[swi];

            while (swj >= 0 && array[swj] > key){
                array[swj + 1] = array[swj];
                swj -= 1;
            }
            array[swj+1] = key;
        }

        return array;
    }
}