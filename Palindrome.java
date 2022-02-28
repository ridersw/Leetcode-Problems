public class Palindrome {
    public static void main(String[] args){
        int n = 12321;

        int rev = reverse(n, 0);

        if (n == rev){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }

    public static int reverse(int number, int temp){
        if (number == 0){
            return temp;
        }

        temp = (temp*10) + (number % 10);
        return reverse(number/ 10, temp);
    }
}   