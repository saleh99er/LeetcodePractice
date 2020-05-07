/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next;} 
}

class mergeTwoLinkedLists {
    //assuming l1 and l2 are never null or empty lists
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // l1 is also our accum list, l1 will always be the lesser head element so if not so swap them
        ListNode temp;
        if(l2.val < l1.val){
                temp = l1;
                l1 = l2;
                l2 = temp;
                System.out.println("Swap occurred");
        } 
        temp = l1;
        while(l1.next != null || l2 != null){
              if(l1.next != null && l2 != null){ // comparison is needed
                  ListNode l1_next = l1.next;
                  if(l2.val < l1_next.val){ // l2 list node needs to be appended to l1
                      System.out.println("Op 1a occurred");
                      l1.next = l2; // insert l2 after l1
                      l2 = l2.next; // adjust l2 to be the next node in l2
                      l1 = l1.next; // adjust l1 to be the node just inserted (originally from l2)
                      l1.next = l1_next; // assign just inserted node's next pointer to be the node that was originally next in l1
                  }
                  else{
                      System.out.println("Op 1b occurred");
                      l1 = l1_next;
                  }
              }
              else if(l2 != null){
                  System.out.println("Op 2 occurred");
                  l1.next = l2; // append rest of l2 to l1
                  l2 = null;
              }
              else{ // l1.next != null then we're done inserting l2 elements, we're done
                System.out.println("Op 3 occurred");
                  break;
              }
        }
        
        return temp;
    }

    public static void main(String[] args){
        ListNode lA = new ListNode(1, new ListNode(3, null));
        ListNode lB = new ListNode(0, new ListNode(2, null));
        ListNode lC = mergeTwoLists(lA, lB);
        while(lC != null){
            System.out.println(lC.val + ",");
            lC = lC.next;
        }
    }
}