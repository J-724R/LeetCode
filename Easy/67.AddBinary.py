class Solution:
    def addBinary(self, a: str, b: str) -> str:
      res = ""
      i, j, carry = len(a) - 1, len(b) - 1, 0
      while i >= 0 or j >= 0:
          sum = carry;
          if i >= 0 : sum += ord(a[i]) - ord('0') # ord is use to get value of ASCII character
          if j >= 0 : sum += ord(b[j]) - ord('0')
          i, j = i - 1, j - 1
          carry = 1 if sum > 1 else 0;
          res += str(sum % 2)

      if carry != 0 : res += str(carry);
      return res[::-1]


# another method found by hridoy100
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int smaller = a.length()-1, larger = b.length()-1;
        if(smaller>larger){
            int tmp = smaller;
            smaller = larger;
            larger = tmp;
            String temp = a;
            a = b;
            b = temp;
        }
        int carry = 0;
        while(larger>=0){
            int ch1 = (smaller>=0)?a.charAt(smaller)-'0':0;
            int ch2 = b.charAt(larger)-'0';
            int sum = ch1 + ch2 + carry;
            // 2 = 10
            if(sum == 2){
                carry = 1;
                sb.append("0");
            }
            // 3 = 11
            else if(sum == 3){
                carry = 1;
                sb.append("1");
            }
            // 1 = 1, or, 0 = 0
            else{
                carry = 0;
                char ch = (char)(sum+'0');
                sb.append(ch);
            }
            smaller--;
            larger--;
        }
        // if there's still one carry left!
        if(carry == 1){
            sb.append("1");
        }
        
        sb.reverse();
        return sb.toString();
    }
}