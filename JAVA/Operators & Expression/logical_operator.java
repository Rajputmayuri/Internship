//Write a program that checks whether a given number lies between 10 and 50 using logical oeprators.
package com.company;
import java.util.Scanner;

public class logical_operator {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number =");
        int a=sc.nextInt();
        boolean result=(a>=10 && a<=50);
        System.out.println(result);
    }
}
