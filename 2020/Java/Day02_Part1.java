import java.io.File;
import java.util.Scanner;

public class Day02_Part1 {
    public static void main(String[] args) {
        try {
            int validity_count = 0;
            // read input
            Scanner scanner = new Scanner(new File("PuzzleInput_Day02.txt"));
            while(scanner.hasNextLine())
            {   
                //    String bounds = scanner.next("\\d+-\\d+");
                //    String character = scanner.next("\\w");
                //    String password = scanner.next(" \\w*$");
                String[] tokens = scanner.nextLine().split(" ");
                String[] bounds = tokens[0].split("-");
                Integer lowerBound  = Integer.valueOf(bounds[0]);
                Integer upperBound  = Integer.valueOf(bounds[1]);
                Character character = tokens[1].charAt(0);
                String password     = tokens[2];


                // chek validity
                // int count = StringUtils.countMatches(password, character);
                int count = 0;
                for (int i=0; i < password.length(); i++) {
                    if (character == password.charAt(i)) {
                        count ++;
                    }
                }
                if ( lowerBound <= count && count <= upperBound ) {
                    validity_count++;
                }
                
                // if ( password.matches(".*" + character + "{" + lowerBound + "," + upperBound + "}" )) {
                //     validity_count++;
                // }
            }
            System.out.println(validity_count);
        } catch(Exception e) {
            System.out.println(e);
        }
        
    }
}
