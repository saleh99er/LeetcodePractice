/** My attempt at Problem 30: Substring with Concatenation of All Words
*/

import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.LinkedList;
import java.util.Set;

class Solution {
    /* 
    n characters in String s
    m words each of which is capped to n characters

    Assuming the m words are not substrings of each other
    ie words = ['hello', 'lo']

    Idea 1:
    could find all substring indices for each word and use the indices
    found to determine whether a combination of the words form in s
    Space: O(m*n) (Relies on 2d int array)
    Time: ???

    Idea 2:
    find how many times a certain word must occur and parse s to see if 
    the occurrences of those substrings without one going over, if so then
    count this index otherwise restart s word occurrences 
    Space:
    Time:

    Idea 3:

    */

    public enum WordOccurStatus {
        FOUND_ALL,
        SEARCH_IN_PROGRESS,
        OVERCOUNT_OCCURRED
    };

    public static WordOccurStatus checkStatus(HashMap<String, Integer> wOccur,
    HashMap<String, Integer> sOccur){
        WordOccurStatus result = WordOccurStatus.FOUND_ALL;
        for( String word : wOccur.keySet()){
            int occurNeeded = wOccur.get(word);
            int occurGotSoFar = sOccur.get(word);
            if(occurGotSoFar > occurNeeded){
                result = WordOccurStatus.OVERCOUNT_OCCURRED;
                return result;
            }
            else if(occurGotSoFar < occurNeeded){
                result = WordOccurStatus.SEARCH_IN_PROGRESS;
            }
        }
        return result;
    }

    public static void resetOccurrences(HashMap<String, Integer> occur){
        occur.replaceAll( (k,v) -> 0);
    }

    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> substringIndices = new LinkedList<Integer>();
        
        // Determine word occurrences needed
        HashMap<String, Integer> wordsOccurrences = new HashMap<String, Integer>(words.length);
        for(String word : words){
            if(wordsOccurrences.containsKey(word)){
                wordsOccurrences.put(word, wordsOccurrences.get(word)+1);
            }
            else {
                wordsOccurrences.put(word, 1);
            }
        }
        int wordsIndex = 0;
        int charIndex = 0;
        HashMap<String, Integer> sOccurrences = new HashMap<String, Integer>(words.length);
        for(String word : words){
            sOccurrences.put(word, 0);
        }
        
        while(charIndex < s.length()){
            System.out.println("iteration of searching thru s, searching = " + s.substring(charIndex));
            int closestSubstringIndex = -1;
            String closestWord = "";

            // Find the next word that occurs in the rest of string S
            for(String word : sOccurrences.keySet()){
                int temp = s.indexOf(word, charIndex);
                if(temp == charIndex){
                    closestWord = word;
                    closestSubstringIndex = temp;
                    break;
                }
                else if (temp < closestSubstringIndex || closestSubstringIndex == -1 ){
                    closestWord = word;
                    closestSubstringIndex = temp;
                }
            }
            if(closestSubstringIndex == -1){
                System.out.println("No substrings found, manually incrementing");
                closestSubstringIndex = charIndex + 1;
            }

            // If next word is at charIndex
            if(closestSubstringIndex == charIndex){
                charIndex = closestSubstringIndex + closestWord.length();
                sOccurrences.put(closestWord, 1 + sOccurrences.get(closestWord));
                
            }
            else{
                charIndex = closestSubstringIndex;
                resetOccurrences(sOccurrences);
                wordsIndex = closestSubstringIndex;
            }

            WordOccurStatus status = checkStatus(wordsOccurrences, sOccurrences);
            switch(status){
                case OVERCOUNT_OCCURRED:
                    resetOccurrences(sOccurrences);
                    wordsIndex = closestSubstringIndex;
                    sOccurrences.put(closestWord, 1);
                    System.out.println("overcount occurred");
                    break;
                case FOUND_ALL:
                    substringIndices.add(wordsIndex);
                    resetOccurrences(sOccurrences);
                    wordsIndex = closestSubstringIndex;
                    System.out.println("found all");
                    break;
                default:
                    break;
            }
        }


        return substringIndices;
    }

    public static void printList(List<Integer> list){
        for(Integer index : list){
            System.out.println("" + index);
        }
        if(list.size() == 0){
            System.out.println("<empty list>");
        }
    }

    public static void main(String[] args){
        String[] words = {"bar", "foo", "the"};
        String s = "barfoofoobarthefoobarman";
        
        System.out.println("----SOLN---------");
        List<Integer> soln = findSubstring(s, words);
        printList(soln);
    }
}