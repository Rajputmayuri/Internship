//Write a program to print multiplication table of a given number n.
//package com.company;
//
//import java.util.Scanner;
//
//public class table {
//    static void main() {
//        Scanner sc=new Scanner(System.in);
//        System.out.print("Enter a number = ");
//        int num=sc.nextInt();
//        for (int i=1;i<=10;i++) {
//            System.out.println(num + " x " + i + " = " + (num * i));
//        }
//
//    }
//}

//----------------------------USING WHILE LOOP----------------------------

package com.company;
import java.util.Scanner;
public class table{
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number =");
        int num=sc.nextInt();
        int i=1;
        while(i<=10){
            System.out.println(num + " X " + i + " = " +(num*i));
            i++;
        }
    }
}