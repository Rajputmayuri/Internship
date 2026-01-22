package com.company;
import java.util.Scanner;
public class ch1_ps1 {
    static void main() {
        //sum of three numbers
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter first number=");
        int a =sc.nextInt();
        System.out.print("Enter second number=");
        int b=sc.nextInt();
        System.out.print("Enter third number=");
        int c=sc.nextInt();
        int sum=a+b+c;
        System.out.println("Sum of three numbers are ="+sum);

    }
}
