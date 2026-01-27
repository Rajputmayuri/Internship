/*Write a java program to fill in a letter template which looks like below.
letter="Dear <|name|>, Thanks a lot"
Replace <|name|> with a string.*/

package com.company;

public class fill_letters {
    static void main() {
        String str="Dear name, Thanks a lot ";
        System.out.println(str.replace("name","Mayuri"));
    }
}
