class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) :
        suffix={}
        for i in range(len(wordsQuery)):
            word = str(wordsQuery[i])
            print(word)
            suffix[i] = ["".join(reversed(word[j:])) for j in range(len(word))]
        print(suffix)
        output = [-1]*len(suffix)
        cont_p=["".join(reversed(s)) for s in wordsContainer]
        print(cont_p)
        ind_suffix =0

        global_best_idx =0
        for i in range(len(cont_p)):
            if len(cont_p[global_best_idx]) > len(cont_p[i]):
                global_best_idx = i

        print(f"global_container_idx :  {global_best_idx}\n")
        output =[]
        for i in range(len(suffix)):
            print(f"\n\nSELECTED SUFFIX: {suffix[i]}")
            best_container_idx = global_best_idx
            longest_length_of_suffix =0
            for j in range(len(cont_p)):
                print(f"\nSELECTED WORD CONTAINER : {cont_p[j]}")
                current_length_of_suffix = 0
                for slice_suffix in suffix[i]:
                    if cont_p[j].startswith(slice_suffix):
                        current_length_of_suffix = len(slice_suffix)
                        print(f"slice : {slice_suffix} matched  , current length : {current_length_of_suffix}")
                        break
                print(f"comparing longest_length {longest_length_of_suffix} with current length : {current_length_of_suffix}")
                if longest_length_of_suffix < current_length_of_suffix:
                    best_container_idx =j
                    longest_length_of_suffix = current_length_of_suffix
                    print(f" best container updated to : {cont_p[j]}")
                    print(f"longest length value updated to : {longest_length_of_suffix}")
                elif longest_length_of_suffix == current_length_of_suffix:
                    print(f"longest length value is equal to current length : {current_length_of_suffix}")
                    if len(cont_p[j]) < len(cont_p[best_container_idx]):
                        best_container_idx = j
                        print(f"lenght of current container : {cont_p[j]} < length of best container : {cont_p[best_container_idx]} , selected : {cont_p[j]}")
            output.append(best_container_idx)
            print(f"\nOUTPUT : {output}\n")    
        return output
        