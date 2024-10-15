class Solution:
    def similarRGB(self, color: str) -> str:
        def closest_component(comp):
            candidates = [i*17 for i in range(16)]
            value = int(comp, 16)
            return min(candidates, key=lambda x: abs(value - x))

        def hexify(n):
            return f'{n:02x}'

        r = color[1:3]
        g = color[3:5]
        b = color[5:7]
        
        closest_r = hexify(closest_component(r))
        closest_g = hexify(closest_component(g))
        closest_b = hexify(closest_component(b))

        return f'#{closest_r}{closest_g}{closest_b}'