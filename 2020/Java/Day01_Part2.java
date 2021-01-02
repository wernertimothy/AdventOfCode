import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.File;

public class Day01_Part2 {
        public static void main(String[] args) {
            // read input
            List<Integer> expense_report = new ArrayList<>();
            try {
                Scanner scanner = new Scanner(new File("PuzzleInput_Day01.txt"));
                while(scanner.hasNextInt())
                {
                    expense_report.add(scanner.nextInt());
                }
            } catch(Exception e) {
                System.out.println(e);
            }
            // bruteforce
            for (Integer a : expense_report) {
                for (Integer b : expense_report) {
                    for (Integer c : expense_report) {
                        if (a + b + c == 2020) {
                            System.out.println(a*b*c);
                            return;
                        }
                    }
                }
            }
        }
}
