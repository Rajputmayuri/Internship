/*Write a java program to print Inverted pyramid.
* * * * * * *
 * * * * *
  * * *
    *
 */
package com.company;

public class Inverted_pyramid {
    static void main() {
        for(int i=4;i>=1;i--){
            for(int space=4;space>i;space--){
                System.out.print(" ");
            }
            for(int star=1;star<=2*i-1;star++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
