/*Write a program to print the following pattern.
*
* *
* * *
* * * *
 */
package com.company;

public class pattern2 {
    static void main() {
        for(int i=1;i<=4;i++){
            for(int j=1;j<=i;j++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
