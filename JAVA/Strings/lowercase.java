//Write a java program to convert a string to lowercase.

package com.company;
import java.util.Scanner;
public class lowercase {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter string :");
        String st=sc.next();
        System.out.println(st.toLowerCase());
    }
}
