class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug_set = set((r, c) for r, c in dig)
        artifact_count = 0

        for r1, c1, r2, c2 in artifacts:
            can_extract = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug_set:
                        can_extract = False
                        break
                if not can_extract:
                    break
            if can_extract:
                artifact_count += 1

        return artifact_count