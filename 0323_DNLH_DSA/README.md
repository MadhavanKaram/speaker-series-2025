# 📢 Dot Net Learners House Meetup – Monthly Event - Mar 2025

## Date Time: 23-Mar-2025 at 09:00 AM IST

## Event URL: [https://www.meetup.com/dot-net-learners-house-hyderabad/events/304750920](https://www.meetup.com/dot-net-learners-house-hyderabad/events/304750920)

## YouTube URL: [https://www.youtube.com/watch?v=rrZqYt2YDFM](https://www.youtube.com/watch?v=rrZqYt2YDFM)

![Information | 50x50](./Documentation/Images/Information.PNG)

![Seat Belt | 50x50](./Documentation/Images/SeatBelt.PNG)

# Two Pointer Algorithm - Valid Palindrome & Three Sum

## **🔹 0-2 min: Introduction to Two Pointer Algorithm (Concept + Advantages)**
The **Two Pointer Algorithm** is an efficient technique used to optimize problems that involve searching, sorting, or working with arrays and strings. Instead of using nested loops, which can be slow, the two-pointer approach allows us to solve problems in linear or near-linear time. This method is particularly useful for problems that involve **pairs, triplets, or subsets** of elements that meet a specific condition.

### **🔹 Why Use Two Pointer Algorithm?**
1. **Reduces Time Complexity** – Instead of `O(n^2)`, it often reduces to `O(n log n)` or `O(n)`.
2. **Memory Efficient** – It does not require extra space apart from a few pointer variables.
3. **Used in Sorted Arrays** – Sorting often enables two-pointer traversal.
4. **Common in Searching & Optimization Problems** – It is frequently used in **palindrome checking, sum problems, merging sorted arrays, and interval problems**.

---

## **✅ 2-5 min: Problem 1 - Valid Palindrome (Concept & Algorithm)**
A **valid palindrome** is a string that reads the same forward and backward after removing non-alphanumeric characters and converting everything to lowercase. 

### **🔸 Algorithm Explanation**
1. **Use Two Pointers:** One at the start (`left`), one at the end (`right`).
2. **Skip Non-Alphanumeric Characters:** Move pointers until they land on valid characters.
3. **Compare Characters:** If they match, move both pointers toward the center.
4. **Repeat Until Pointers Meet:** If all pairs match, the string is a palindrome; otherwise, it is not.

### **🔹 Python Code**
```python
def is_palindrome(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
```

### **🔹 Java Code**
```java
class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int left = 0, right = s.length() - 1;
        
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isPalindrome("A man, a plan, a canal: Panama"));  // Output: True
    }
}
```

**Complexity:**
- **Time:** `O(n)` – Single pass over string
- **Space:** `O(1)` – No extra space used

---

## **✅ 5-10 min: Problem 2 - Three Sum (Concept & Algorithm)**
The **Three Sum** problem requires finding unique triplets `(a, b, c)` in an array where `a + b + c = 0`. The naive approach using three nested loops (`O(n^3)`) is inefficient for large arrays. Instead, **sorting + two pointers** gives a better solution in `O(n^2)`.

### **🔸 Algorithm Explanation**
1. **Sort the Array:** Sorting helps efficiently find pairs that sum to a target value.
2. **Iterate Through Array:** Fix one element at index `i`.
3. **Two Pointer Search:** Set `left = i + 1` and `right = len(nums) - 1`.
4. **Check Sum:**
   - If `nums[i] + nums[left] + nums[right] == 0`, store the triplet.
   - If sum is **too small**, move `left` right.
   - If sum is **too large**, move `right` left.
5. **Skip Duplicates:** To ensure unique triplets, skip repeated elements.

### **🔹 Python Code**
```python
def three_sum(nums):
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res

print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
```

### **🔹 Java Code**
```java
import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int left = i + 1, right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < 0) left++;
                else right--;
            }
        }
        return result;
    }
}
```

**Complexity:**
- **Sorting:** `O(n log n)`
- **Two-pointer traversal:** `O(n^2)`
- **Overall Complexity:** `O(n^2)`

---

## **✅ 10-15 min: Summary & Conclusion**
| Problem | Time Complexity | Space Complexity |
|---------|---------------|----------------|
| **Valid Palindrome** | `O(n)` | `O(1)` |
| **Three Sum** | `O(n^2)` | `O(1)` (Ignoring output space) |

The **Two Pointer Algorithm** is a powerful approach for reducing complexity in array and string problems. It eliminates unnecessary iterations and is widely used in **searching, sorting, and optimization problems**. Understanding its application in different scenarios will help you solve problems faster and more efficiently! 🚀
