public class JavaBubbleSort{
    public static void main(String args[]){
        int[] array = {6,5,4,3,2,1};

        int[] result = bubbleS(array);

        for(int swi=0; swi<result.length;swi++){
            System.out.print(result[swi] + " ");
        }
    }

    public static int[] bubbleS(int[] array){

        for (int swi = 0; swi < array.length-1;swi++){
            for (int swj =swi+1;swj < array.length;swj++){
                if (array[swj] < array[swi]){
                    int temp = array[swi];
                    array[swi] = array[swj];
                    array[swj] = temp;
                }
            }
        }

        return array;
    }
}