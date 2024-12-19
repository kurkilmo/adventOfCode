import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class Day11 {
    public static void main(String[] args) {
        String filename = "input.txt";
        Scanner scn = null;
        try {
            scn = new Scanner(new File(filename));
        } catch (FileNotFoundException e) {
            System.out.println("ei tiedostoo");
            System.out.println(e.getMessage());
            System.exit(1);
        }

        List<Long> nums = new ArrayList<>();

        String line = scn.nextLine();
        scn.close();
        for (String str : line.split(" ")) {
            nums.add(Long.parseLong(str));
        }
        
        int iterations = 75;

        for (long it = 0; it < iterations; it++) {
            System.out.println("Iteration: " + it);
            // System.out.println(nums.toString());
            int i = 0;
            while (i < nums.size()) {
                long value = nums.get(i);
                if (value == 0) nums.set(i, (long) 1);
                else if (String.valueOf(value).length() % 2 == 0) {
                    String str = String.valueOf(value);
                    int length = str.length() / 2;
                    String first = str.substring(0, length);
                    String last = str.substring(length, str.length());

                    nums.add(i, Long.parseLong(first));
                    i++;
                    nums.set(i, Long.parseLong(last));
                } else {
                    nums.set(i, value * 2024);
                }
                i++;
            }
        }

        System.out.println("Length: " + nums.size());
    }
}