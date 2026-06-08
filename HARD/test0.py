class Solution1:
    def stringIndices1(self, wordsContainer , wordsQuery ) :
        suffix={}
        for i in range(len(wordsQuery)):
            word = str(wordsQuery[i])
            # print(word)
            suffix[i] = ["".join(reversed(word[j:])) for j in range(len(word))]
        # print(suffix)
        output = [-1]*len(suffix)
        cont_p=["".join(reversed(s)) for s in wordsContainer]
        # print(cont_p)
        ind_suffix =0

        global_best_idx =0
        for i in range(len(cont_p)):
            if len(cont_p[global_best_idx]) > len(cont_p[i]):
                global_best_idx = i

        # print(f"global_container_idx :  {global_best_idx}\n")
        output =[]
        for i in range(len(suffix)):
            # print(f"\n\nSELECTED SUFFIX: {suffix[i]}")
            best_container_idx = global_best_idx
            longest_length_of_suffix =0
            for j in range(len(cont_p)):
                # print(f"\nSELECTED WORD CONTAINER : {cont_p[j]}")
                current_length_of_suffix = 0
                for slice_suffix in suffix[i]:
                    if cont_p[j].startswith(slice_suffix):
                        current_length_of_suffix = len(slice_suffix)
                        # print(f"slice : {slice_suffix} matched  , current length : {current_length_of_suffix}")
                        break
                # print(f"comparing longest_length {longest_length_of_suffix} with current length : {current_length_of_suffix}")
                if longest_length_of_suffix < current_length_of_suffix:
                    best_container_idx =j
                    longest_length_of_suffix = current_length_of_suffix
                    # print(f" best container updated to : {cont_p[j]}")
                    # print(f"longest length value updated to : {longest_length_of_suffix}")
                elif longest_length_of_suffix == current_length_of_suffix:
                    # print(f"longest length value is equal to current length : {current_length_of_suffix}")
                    if len(cont_p[j]) < len(cont_p[best_container_idx]):
                        best_container_idx = j
                        # print(f"lenght of current container : {cont_p[j]} < length of best container : {cont_p[best_container_idx]} , selected : {cont_p[j]}")
            output.append(best_container_idx)
            # print(f"\nOUTPUT : {output}\n")    
        return output
    

# OPTIMIZED CODE 
class TrieNode:
    def __init__ (self,best_idx):
        self.best_idx = best_idx
        self.children ={}        
class Solution2:
    def stringIndices2(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        #finding the global best idx
        ans =[]
        global_best_idx =0
        for i in range(len(wordsContainer)):
            if len(wordsContainer[global_best_idx])>len(wordsContainer[i]):
                global_best_idx = i
        # print("GLOBAL BEST IDX FOUND TO BE : ",wordsContainer[global_best_idx])

        # building the tree 
        # print("\n BUILDING TREE \n")
        root = TrieNode(global_best_idx)
        for i,word in enumerate(wordsContainer):
            node = root
            # print("\nCURRENT WORD : ", word)
            # print("currently at root")
            for char in reversed(word):
                # print(f"current character : {char}")
                if char not in node.children:
                    node.children[char] = TrieNode(i)
                    # print(f"created a new node {char} best idx is {i}")
                node = node.children[char]
                # print(f"current positiion changed to {char}")
                if len(word) < len (wordsContainer[node.best_idx]):
                    # print(f"best idx for {char} changed to {i}")
                    node.best_idx = i


        #QUERY SEARCH
        # print("\n\nFINDING THE LONGEST COMMON SUFFIX \n")
        for word in wordsQuery:
            node = root
            # print(f" CURRENT WORD : {word}")
            for char in reversed(word):
                # print(f"current char : {char}")
                if char in node.children:
                    node = node.children[char]
                    # print(f"found moving to next char")
                else:
                    # print(f"terminated ")
                    break
            # print(f"\n best idx for {word} is : {node.best_idx}")
            ans.append(node.best_idx)
        return ans

    
        











#INPUTS

sol_optimized = Solution2()
sol_custom = Solution1()

# --- Test Case 1: Standard Case (Example 1 from description) ---
wordsContainer1 = ["abcd", "bcd", "xbcd"]
wordsQuery1 = ["cd", "bcd", "xyz"]
print("--- Test Case 1 ---")
print(f"Optimized Code Output: {sol_optimized.stringIndices2(wordsContainer1, wordsQuery1)}")
print(f"Your Custom Code Output: {sol_custom.stringIndices1(wordsContainer1, wordsQuery1)}")
print("Expected Output:        [1, 1, 1]\n")


# --- Test Case 2: Multi-character match with length tie-breaker (Example 2) ---
wordsContainer2 = ["abcdefgh", "poiuygh", "ghghgh"]
wordsQuery2 = ["gh", "acbfgh", "acbfegh"]

print("--- Test Case 2 ---")
print(f"Optimized Code Output: {sol_optimized.stringIndices2(wordsContainer2, wordsQuery2)}")
print(f"Your Custom Code Output: {sol_custom.stringIndices1(wordsContainer2, wordsQuery2)}")
print("Expected Output:        [2, 0, 2]\n")


# --- Test Case 3: Complete Fallback (No matching suffixes at all) ---
wordsContainer3 = ["apple", "cat", "dog"]
wordsQuery3 = ["xyz", "mno"]

print("--- Test Case 3 ---")
print(f"Optimized Code Output: {sol_optimized.stringIndices2(wordsContainer3, wordsQuery3)}")
print(f"Your Custom Code Output: {sol_custom.stringIndices1(wordsContainer3, wordsQuery3)}")
print("Expected Output:        [1, 1]  (Both fall back to 'cat' at index 1 because it is shortest/earliest)")