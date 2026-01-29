/*Write a java program to print Repeated Number Pattern.
1
2 2
3 3 3
4 4 4 4
 */
package com.company;

public class Repeated_number_pattern {
    static void main() {
        for(int i=1;i<=4;i++){
            for(int j=1;j<=i;j++){
                System.out.print(i +" ");
            }
            System.out.println();
        }
    }
}
