
class Solution:
    def evaluate(self, expression: str) -> int:
        stack = []
        parenEnd = {}
        
        for idx, ch in enumerate(expression):
            if ch == '(':
                stack.append(idx)
            if ch == ')':
                parenEnd[stack.pop()] = idx

        def parse(lo, hi):
            arr = []
            word = []

            i = lo
            while i < hi:
                if expression[i] == '(':
                    arr.append(parse(i + 1, parenEnd[i]))
                    i = parenEnd[i]
                elif expression[i] == ' ' or expression[i] == ')' and word != []:
                    if ''.join(word) != '':
                        arr.append(''.join(word))
                    word = []
                    i += 1
                elif expression[i] != ')':
                    word.append(expression[i])
                    i += 1
                else:
                    i += 1


            if word != []:
                arr.append(''.join(word))

            return arr

        expressionList = parse(1, len(expression) - 1)

        return self.genEval(expressionList, {})
    
    def genEval(self, expression, scope):
        if type(expression) != list:
            try:
                return int(expression)
            except:
                return scope[expression]
        else:
            if expression[0] == 'let':
                expression = expression[1:]
                
                while len(expression) > 2:
                    scope = self.letEval(expression, scope.copy())
                    expression = expression[2:]
                    
                return self.genEval(expression[0], scope.copy())
                
            if expression[0] == 'add':
                return self.addEval(expression, scope.copy())
                
            if expression[0] == 'mult':
                return self.multEval(expression, scope.copy())


    
    def letEval(self, expression, scope):
        scope[expression[0]] = self.genEval(expression[1], scope)
        return scope
    
    def addEval(self, expression, scope):
        return self.genEval(expression[1], scope) + self.genEval(expression[2], scope)
    
    def multEval(self, expression, scope):
        return self.genEval(expression[1], scope) * self.genEval(expression[2], scope)

