/*Print right-Aligned triangle.
      *
    * *
  * * *
* * * *

 */
package com.company;
public class pattern5 {
    static void main() {
        for (int i = 1; i <= 4; i++) {
            for (int space = 4; space > i; space--) {
                System.out.print("  ");
            }
            for (int star = 1; star <= i; star++) {
                System.out.print("* ");
            }
            System.out.println();
        }

    }
}
