//Reverse String
package com.company;

import java.util.Scanner;

public class reverse_string {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a string = ");
        String str=sc.nextLine();

        String rev="";

        for(int i=str.length()-1;i>=0;i--){
            rev=rev+str.charAt(i);
        }
        System.out.println("Reverse String :"+rev);
    }
}
