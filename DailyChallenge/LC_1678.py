# 1678. Goal Parser Interpretation
class Solution:
    def interpret(self, command: str) -> str:
        
        result = command.replace("()", "o")
        
        # Make sure have "result" as the string you want to CONTINUE modify the previous modified string (NOT "command")
        result = result.replace("(al)", "al")
        
        return result
        # return command.replace("()", "o").replace("(al)", "al")
        
