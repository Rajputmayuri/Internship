package com.company;

public class grade_encrypt_decrypt {
    static void main() {
        //Write a java program to encrypt a grade by adding 8 bit to it. Decrypt it to show the correct grade.
        //encrypt
        char grade='B';
        grade=(char)(grade+8);
        System.out.println(grade);

        //decrypt
        grade=(char)(grade-8);
        System.out.println(grade);
    }
}
