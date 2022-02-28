public class Summation1{
    public static void main(String args[]){
        int[] array = {6,1,3,9,6,2,4,5,3,1};

        int result = summ(array, 1);

        System.out.println("Result: " + result);
    }

    public static int summ(int[] array, int pointer){
        if (pointer == array.length-1){
            array[pointer] += array[pointer-1];
            return array[array.length-1];
        }

        array[pointer] += array[pointer-1];
        
        return summ(array, pointer + 1);
    }
}

