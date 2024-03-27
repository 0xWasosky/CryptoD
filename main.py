import secrets



class CryptoD:
    @staticmethod
    def encrypt(string: str):
        divisor = secrets.token_urlsafe(16 * 7)
        data = ""
        data += divisor[0:75]

        for index, char in enumerate(string):
            data += chr(ord(char) + index)
        data += divisor[75:150]
        return data, len(string) * len(data)
    
    @staticmethod
    def decyprt(string: str, key: int):

       data = list(string)[75:int(key / len(string)) + 75]
       return "".join(chr(ord(char) - index) for (index, char ) in enumerate(data))
