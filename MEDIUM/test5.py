# Problem Description

# You are building a pyramid of colored blocks. Each block is represented by a single capital letter (from 'A' to 'G').

# The pyramid is built from the bottom up, row by row:

# You start with a given string bottom which acts as the entire base row of the pyramid.

# Every new row you build on top must contain exactly one less block than the row beneath it, with the blocks centered on top of the pairs below.

# To place a block on top of two adjacent blocks, the resulting 3-block triangle pattern must be listed in your rulebook array, called allowed.

# A pattern in allowed is written as a 3-letter string like "ABC". This means if you have 'A' on the left bottom and 'B' on the right bottom, you are allowed to place 'C' on top of them.

# Your goal is to determine if you can successfully build the pyramid all the way up to a single block at the top apex using the rules provided. Return true if you can reach the top, and false otherwise.






#APPROACH 1 
class Solution1:
    def pyramidTransition1(self, bottom: str, allowed: List[str]) -> bool:
        transition_map ={}
        for string in allowed:
            key = string[:2]
            value = string[2]
            if key not in transition_map:
                transition_map[key] = []
            transition_map[key].append(value)
        print(transition_map)
        memory ={} 

        def can_build(current,next,index):
            if len(current) == 1:
                return True

            if len(next) == len(current)-1:
                if next in memory:
                    return memory[next]

                else:
                    res = can_build(next,"",0)
                    memory[next] = res
                    return res
            string = current[index:index+2]
            if string in transition_map:
                allowed_tops = transition_map[string]
            else:
                allowed_tops =[]
            for top in allowed_tops:
                if can_build(current,next+top,index+1):
                    return True
            return False
        res = can_build(bottom,"",0)
        return res

#APPROACH 2 (SAME METHOD , BUT USES 2D LIST INSTEAD OF HASHMAP AND USES NUMERICAL COMAPRISON RATHER THAN STRING COMPARISON)
class Solution2:
    def pyramidTransition2(self, bottom: str, allowed: List[str]) -> bool:
        def char_to_int(ch) -> int:
            return ord(ch) - ord("A")

        transition_matrix =[[[]for _ in range(9)] for _ in range(9)]
        
        for string in allowed:
            u=char_to_int(string[0])
            v=char_to_int(string[1])
            w=char_to_int(string[2])

            transition_matrix[u][v].append(w)
        
        cannot_proceed = set()
        def can_build(current,next,index):
            if len(current) == 1 :
                return True
            if len(next) == len(current)-1 :
                print 
                next = tuple(next)
                if next in cannot_proceed:
                    return False
                elif can_build(next,[],0):
                    return True
                else :
                    cannot_proceed.add(next)
                    return False
            allowed_tops = transition_matrix[current[index]][current[index+1]]
            for tops in allowed_tops:
                next.append(tops)
                if can_build(current,next,index+1):
                    return True
                next.pop()
            return False

        current = [char_to_int(c) for c in bottom]
        return can_build(current,[],0)

