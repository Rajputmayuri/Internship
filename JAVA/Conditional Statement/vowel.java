//Write a java program to check whether a character entered by the user is a vowel or consonant.

package com.company;

import java.util.Scanner;

public class vowel {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a character =");
        char character=sc.next().charAt(0);  //It reads a word from the user, extracts its first character, and stores it in the variable ch.
        if (character=='a' || character=='e' || character=='i' || character=='o' ||
        character=='u' ||character=='A' || character=='E' || character=='I'|| character
        =='O' || character=='U') {
            System.out.println("Vowel");
        }
        else {
            System.out.println("Consonant");
        }
    }
}
