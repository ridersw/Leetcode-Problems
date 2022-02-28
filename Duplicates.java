import java.security.Key;
import java.util.Dictionary;
import java.util.Hashtable;

public class Duplicates{
    public static void main(String args[]){
        int[] array = {1,2,3,3,3,4,5,6,7,8,9};

        // Hashtable<Integer, Integer> dict = new Hashtable<>();

        Hashtable<Integer, Integer> dict = new Hashtable<>();

        for (int swi=0;swi<array.length;swi++){
            if (dict.containsKey(array[swi])){
                int val = dict.get(array[swi]) + 1;
            dict.put(array[swi], val);
            }
            else{
                dict.put(array[swi], 1);
            }
        }

        System.out.println(dict);
        int num;
        int freq = 0;
        for (Integer Key: dict.keySet()){
            System.out.println("Key: " + Key + "  Value: " + dict.get(Key));
        }

    }
}