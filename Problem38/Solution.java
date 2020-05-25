// My attempt at Problem 38: Count and Say, 0ms "faster than 100% of submissions" but less memory (36.6 MB) than 52.63% of submissions

import java.lang.StringBuilder;

class Solution {
    public static String counter(String prevString, int stepsLeft){
        if(stepsLeft == 0){
            return prevString.toString();
        }
        else{
            StringBuilder currentString = new StringBuilder();
            char lastCharSeen = prevString.charAt(0);
            int consecutiveSeen = 1;

            //System.out.println( "prevString =  " + prevString.toString() + "  length:" + prevString.length());
            for(int i = 1; i < prevString.length(); i++){
                char prevChar = prevString.charAt(i);
                if(lastCharSeen == prevChar){
                    consecutiveSeen++;
                }
                else{
                    currentString.append(consecutiveSeen);
                    currentString.append(lastCharSeen);
                    consecutiveSeen = 1;
                    lastCharSeen = prevChar;
                }
            }
            currentString.append(consecutiveSeen);
            currentString.append(lastCharSeen);

            return counter(currentString.toString(), stepsLeft-1);
        }
    }    

    public static String countAndSay(int n) {
        String start = "1";
        return counter(start, n-1);
    }

    public static void main(String[] args){
        System.out.println(countAndSay(5));
    }
}