class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        
        n = len(message)

        # First determine the length of thingie
        x = 1
        # Number of msgs needed
        msgCount = 0

        # Computes msgCount and its length respectivaly if possible
        while True:
            if (3 + 2 * x) >= limit: # suffix exceeds limit
                # unable to find a number of msgs
                return []
            

            # With msgCount of length x, find what msgCount it could be 
            def getMsgCount(x):
                msgCount = 0
                total = 0 # max possible msg length
                for i in range(x):
                    numMsg = 9 * (10 ** i) # number of messages of length i
                    suffixLen = 3 + x + (i + 1) # length of suffix needed
                    lenForMsg = limit - suffixLen # available length for actual message
                    total += numMsg * lenForMsg

                    if total >= n: # We know now number of msg has thingie of length x:
                        total -= numMsg * lenForMsg # time to figure out min msg needed
                        remaining = n - total
                        extraNeeded = remaining // lenForMsg + (remaining % lenForMsg > 0) # extra msgs of thingie length i
                        msgCount += extraNeeded # We now have number of msgsNeeded, can break
                        return msgCount
                    else:
                        msgCount += numMsg # Otherwise we continue to keep track of numMsg
                
                return 0
            
            msgCount = getMsgCount(x)
            if msgCount != 0:
                break

            x += 1 # increase length needed

        # print(x)
        # print(msgCount)

        # Build output
        output = []
        a = 0 # pointer for string
        currMsgCount = 1

        for i in range(x - 1):
            numMsg = 9 * (10 ** i) # number of messages of length i
            suffixLen = 3 + x + (i + 1) # length of suffix needed
            lenForMsg = limit - suffixLen # available length for actual message

            for _ in range(numMsg):
                output.append(message[a:a + lenForMsg] + f"<{currMsgCount}/{msgCount}>")
                currMsgCount += 1
                a += lenForMsg
        
        # Finally, rest of messages

        while currMsgCount <= msgCount:
            suffixLen = 3 + 2 * x # length of suffix needed
            lenForMsg = limit - suffixLen # available length for actual message
            output.append(message[a:a + lenForMsg] + f"<{currMsgCount}/{msgCount}>")
            a += lenForMsg
            currMsgCount += 1

        return output