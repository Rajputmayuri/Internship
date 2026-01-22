package com.company;
import java.util.Scanner;
public class ch1_ps3 {
    static void main() {
        //Write a program which asks the user to enter his/her name and greets them with "Hello <name>, have a good day" text.
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter your name =");
        String str= sc.next();
        System.out.println("Hello "+str+", have a good day.");
    }
}
