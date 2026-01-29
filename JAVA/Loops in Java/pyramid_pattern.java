/*Write a java program to print the pyramid pattern
        *
      * * *
    * * * * *
  * * * * * * *
 */
package com.company;

public class pyramid_pattern {
    static void main() {
        for(int i=1;i<=4;i++){
            for (int space=4;space>i;space--){
                System.out.print(" ");
            }
            for(int star=1;star<=2*i-1;star++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
