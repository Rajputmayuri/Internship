package com.company;
import java.util.Scanner;

public class TakingInput {
    static void main() {
        System.out.println("Taking input from the user!");
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter first number =");
        int a=sc.nextInt();
        System.out.print("Enter second number =");
        int b=sc.nextInt();
        int sum=a+b;
        System.out.print("The sum of two number is =");
        System.out.println(sum);
    }
}
