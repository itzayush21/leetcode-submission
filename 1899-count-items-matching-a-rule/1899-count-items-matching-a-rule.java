class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int key=0,count=0;

        if(ruleKey.equals("type"))
        {
            key=0;
        }
        else if(ruleKey.equals("color"))
        {
            key=1;
        }
        else
        {
            key=2;
        }
        System.out.println(key);
        for(List e:items)
        {
            if(e.get(key).equals(ruleValue))
            {
                count+=1;
            }
        }
        return count;
        
    }
}