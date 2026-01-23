package com.company;
import java.util.Scanner;
public class arithmetic_operators {
    static void main() {
        //Write a java program to take two integers as input and display their sum, difference, product, quotient, and remainder using arithmetic operators.
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter first number =");
        int num1=sc.nextInt();
        System.out.print("Enter second number =");
        int num2=sc.nextInt();
        int sum=num1+num2;
        System.out.println("Sum of numbers are="+sum);
        int diff=num1-num2;
        System.out.println("Difference of numbers are="+diff);
        int prod=num1*num2;
        System.out.println("Product of numbers are="+prod);
        int quotient=num1/num2;
        System.out.println("Quotient of numbers are="+quotient);
        int remainder=num1%num2;
        System.out.println("Remainder of numbers are="+remainder);


    }
}
//----------------------------------------------

/*import java.util.Scanner;

class ArithmeticOperations {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println("Sum = " + (a + b));
        System.out.println("Difference = " + (a - b));
        System.out.println("Product = " + (a * b));
        System.out.println("Quotient = " + (a / b));
        System.out.println("Remainder = " + (a % b));
    }
}
*/