//Write a java program to check whether a number is even or odd using the modulus (%) operator.

package com.company;
import java.util.Scanner;
public class modulus_operator {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number =");
        int num=sc.nextInt();
        if (num%2==0)
            System.out.println("EVEN");
        else
            System.out.println("ODD");
    }
}
