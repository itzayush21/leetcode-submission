class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] s1 = sentence1.split(" ");
        String[] s2 = sentence2.split(" ");

        if(s1.length>s2.length)
        {
            String[] temp=s1;
            s1=s2;
            s2=temp;
        }

        int l1=0,l2=0;
        while(l1<s1.length && l2<s2.length && s1[l1].equals(s2[l2]))
        {
            l1++;l2++;
        }
        int r1=s1.length-1,r2=s2.length-1;
        while(r1>=0 && r2>=0 && s1[r1].equals(s2[r2]))
        {
            r1--;r2--;
        }

        return l1>r1;

    }
}