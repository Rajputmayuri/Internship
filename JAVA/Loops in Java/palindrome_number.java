//Write a program to check whether a number is palindrome or not.
package com.company;

import java.util.Scanner;

public class palindrome_number {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number =");
        int n=sc.nextInt();

        int rev=0;
        int original=n;

        while(n>0){
            int digit=n%10;
            rev=rev*10+digit;
            n/=10;
        }
        if(rev==original){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not Palindrome");
        }
    }
}
