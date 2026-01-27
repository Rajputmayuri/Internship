//Write a java program to find the greater of two numbers entered by the user.

package com.company;

import java.util.Scanner;

public class greater_number {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter 1st number =");
        int num1=sc.nextInt();
        System.out.print("Enter 2nd number =");
        int num2=sc.nextInt();
        if (num1>num2) {
            System.out.printf("%d is greater ",num1);
        }
        else{
            System.out.printf("%d is greater ",num2);
        }
    }
}
