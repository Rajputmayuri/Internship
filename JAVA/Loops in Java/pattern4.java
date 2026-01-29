/*Print a square star pattern of size n.
* * * *
* * * *
* * * *
* * * *
 */
package com.company;

import java.util.Scanner;

public class pattern4 {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter n =");
        int n=sc.nextInt();
        for (int i=1;i<=n;i++){
            for(int j=1;j<=4;j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
