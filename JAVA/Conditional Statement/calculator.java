//Write a java program to implement a simple calculator using switch statement.

package com.company;

import java.util.Scanner;

public class calculator {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter 1st number =");
        double num1=sc.nextDouble();
        System.out.print("Enter 2nd number =");
        double num2=sc.nextDouble();
        System.out.print("Enter an operator (+,-,*,/) = ");
        char operator =sc.next().charAt(0);

        switch(operator){
            case '+':
                System.out.println("Result ="+(num1+num2));
                break;
            case '-':
                System.out.println("Result ="+(num1-num2));
                break;
            case '*':
                System.out.println("Result ="+(num1*num2));
                break;
            case '/':
                System.out.println("Result ="+(num1/num2));
                break;
            default:
                System.out.println("Invalid operator ");

        }
        }


    }

