import java.util.Arrays;

public class Radix{
    public static void main(String args[]){
        int[] array = { 170, 45, 75, 90, 802, 24, 2, 66 };
        
        int len = array.length;

        radixSort(array);
        print(array);

    }

    public static void print(int[] array){
        for(int swi=0;swi<array.length;swi++){
            System.out.print(array[swi] + " ");
        }
    }

    public static void radixSort(int[] array){
        int m = getMax(array);

        for (int exp = 1; (m/exp) > 1;exp *= 10){
            countSort(array, exp);
        }
    }

    public static int getMax(int[] array){
        int max = array[0];

        for (int swi=0;swi<array.length;swi++){
            if (array[swi] > max){
                max = array[swi];
            }
        }

        return max;
    }

    public static void countSort(int[] array, int exp){
        int n = array.length;
        int[] output = new int[n];

        int swi;

        int count[] = new int[n];

        Arrays.fill(count, 0);

        for(swi=0; swi<n;swi++){
            count[(array[swi]/exp) % 10]++;
        }

        for(swi=0;swi<10;swi++){
            count[swi] += count[swi-1];
        }

        for(swi=n-1;swi>=0;swi--){
            output[count[(array[swi]/exp)%10]-1] = array[swi];
            count[(array[swi]/exp)%10]--;
        }

        for (swi=0;swi< n;swi++){
            array[swi] = output[swi];
        }
    }
}