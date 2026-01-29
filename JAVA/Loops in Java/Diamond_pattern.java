/*Write a java program to print Diamond pattern.
      *
    * * *
  * * * * *
    * * *
      *
 */
package com.company;

public class Diamond_pattern {
    static void main() {
        for(int i=1;i<=3;i++){
            for(int s=3;s>i;s--) System.out.print(" ");
            for(int j=1;j<=2*i-1;j++) System.out.print("* ");
            System.out.println();
        }
        for(int i=2;i>=1;i--){
            for(int s=3;s>i;s--) System.out.print(" ");
            for(int j=1;j<=2*i-1;j++) System.out.print("* ");
            System.out.println();
        }
    }
}
