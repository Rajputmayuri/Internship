//Write a program to check whether a number is prime or not.
package com.company;

import java.util.Scanner;

public class prime_number {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter number =");
        int n=sc.nextInt();

        int count=0;
        if(n<=1) {
            System.out.println(n + " is not a prime number ");
        }else{
            for(int i=1;i<=n;i++){
                if(n%i==0){
                    count++;
                }
            }
            if(count==2){
                System.out.println(n +" is a prime number");
            }
            else{
                System.out.println(n+" is not a prime number");
            }

        }
    }
}
