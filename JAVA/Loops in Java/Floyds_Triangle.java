/*Wirte a java program to print Floyd's Triangle
1
2 3
4 5 6
7 8 9 10
 */
package com.company;

public class Floyds_Triangle {
    static void main() {
        int num=1;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=i;j++){
                System.out.print(num+ " ");
                num++;
            }
            System.out.println();
        }
    }
}
