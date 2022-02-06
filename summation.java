public class summation{

    public static int getSummation(int[] array){
        int answer = 0;

        int len = array.length;

        for(int swi=0;swi<len;swi++){
            answer += array[swi];
        }

        return answer;
    }
    public static void main(String[] args){
        int[] array = {1,2,3,4,5,6,7,8,9,10};

        int answer = getSummation(array);
        System.out.println("Answer: " + answer);
    }
}