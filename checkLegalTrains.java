import java.util.Scanner;

public class checkLegalTrains {
    public static void main(String[] args) {
        int swi  = 0, length;
        String trains;

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Train for Validation: ");

        trains = sc.nextLine();
        length = trains.length();

        if(trains.charAt(0) == 'E' && trains.charAt(1) == 'E'){
            swi = 2;
        }else if(trains.charAt(0) == 'E'){
            swi = 1;
        }else{
            System.out.println("The train is not Good Train: Train Rejected");
        }

        if(!(trains.charAt(swi) == 'T')){
            System.out.println("The train is not Good Train: Train Rejected");
            return;
        }
        swi =swi+ 1;

        for(;swi<length-1;swi++){
            if(!(trains.charAt(swi) == 'T')){
                System.out.println("The train is not Good Train: Train Rejected");
                return;
            }
        }

        if(trains.charAt(length-1) == 'G'){
            System.out.println("The train is a Good Train: Train Accepted");
        }else {
            System.out.println("EEThe train is not Good Train: Train Rejected");
        }
        return;
    }
}
