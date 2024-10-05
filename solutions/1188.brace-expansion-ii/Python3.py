class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        import re
        from functools import reduce

        def product(set1, set2):
            return {s1 + s2 for s1 in set1 for s2 in set2}

        def merge(sets):
            return reduce(lambda x, y: x | y, sets, set())

        def parse(expression):
            stack = []
            current_set = set()
            brace_level = 0

            for i, c in enumerate(expression):
                if c == '{':
                    if brace_level == 0:
                        start = i
                    brace_level += 1
                elif c == '}':
                    brace_level -= 1
                    if brace_level == 0:
                        internal_set = parse(expression[start + 1:i])
                        if current_set:
                            current_set = product(current_set, internal_set)
                        else:
                            current_set = internal_set
                elif c == ',':
                    if brace_level == 0:
                        stack.append(current_set)
                        current_set = set()
                elif brace_level == 0 and c.isalpha():
                    if current_set:
                        current_set = product(current_set, {c})
                    else:
                        current_set.add(c)

            if brace_level == 0:
                stack.append(current_set)

            return merge(stack)

        result = parse(expression)
        return sorted(result)