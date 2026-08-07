class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        pointer = 0

        while pointer < len(s):
            delimiter = pointer
            while s[delimiter] != "#":
                delimiter +=1
            length = int(s[pointer: delimiter])
            pointer = delimiter + 1
            decoded.append(s[pointer: pointer + length])
            pointer += length
        return decoded