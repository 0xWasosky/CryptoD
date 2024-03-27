import secrets



class CryptoD:
    def __init__(self, lenght: int) -> None:
        self.random_bytes_lenght = lenght

    def encrypt(self, string: str):
        divisor = secrets.token_urlsafe(self.random_bytes_lenght)
        data = ""
        data += divisor[0:self.random_bytes_lenght // 2]

        for index, char in enumerate(string):
            data += chr(ord(char) + index)
        data += divisor[self.random_bytes_lenght // 2:self.random_bytes_lenght]
        return data, len(string) * len(data)
    
    def decyprt(self, string: str, key: int):

       data = list(string)[self.random_bytes_lenght // 2:int(key / len(string)) + self.random_bytes_lenght // 2]
       return "".join(chr(ord(char) - index) for (index, char ) in enumerate(data))
