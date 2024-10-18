class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        w_revs = sorted((w[::-1], i) for i, w in enumerate(wordsContainer))
        W, non_match_idx = len(wordsContainer), sorted((len(w), i) for i, w in enumerate(wordsContainer))[0][1]
        
        ans, known_pfxs = [], {}
        for q in wordsQuery:
            qr = q[::-1]    # reverse the query string

            # iterate through all possible substring prefixes in decreasing length
            for sz in range(len(qr), 0, -1):
                pfx = qr[:sz]   # current prefix substring
                
                # check cached prefixes
                if pfx in known_pfxs:
                    ans.append(known_pfxs[pfx])
                    break
                
                # find first potential match of current prefix substring in sorted & reversed words-container
                res = idx = bisect.bisect_left(w_revs, (pfx, -1))
                
                # check through all words in sorted & reversed words-container that matched the prefix
                # substring; and find the word which should be used as the matching text for the query
                while idx < W and w_revs[idx][0].startswith(pfx):
                    # the new word that matches the prefix is shorter OR of same length but has a smaller index
                    if (len(w_revs[idx][0]) < len(w_revs[res][0]) or
                        len(w_revs[idx][0]) == len(w_revs[res][0]) and w_revs[idx][1] < w_revs[res][1]):
                        res = idx
                    idx += 1
                
                # if the current index in words-container indeed matches the query, then add it to the running answer
                if res < W and w_revs[res][0].startswith(pfx):
                    known_pfxs[pfx] = w_revs[res][1]
                    ans.append(known_pfxs[pfx])
                    break
            else:
                # no matching prefix found at all, thus add the non-match result
                ans.append(non_match_idx)
        
        return ans