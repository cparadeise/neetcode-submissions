class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder("");
        String separator = "#";

        for (String s : strs) {
            encoded.append(s.length());
            encoded.append(separator);
            encoded.append(s);
        }

        return encoded.toString();
    }

    public List<String> decode(String encodedStr) {
        List<String> decodedWords = new ArrayList<>();
        String separator = "#";
        int pointer = 0;

        while (pointer < encodedStr.length()) {
            // Find the next delimiter "#"
            int delimiter = encodedStr.indexOf(separator, pointer);
            
            // Extract the length of the word
            String lengthStr = encodedStr.substring(pointer, delimiter);
            int length = Integer.parseInt(lengthStr);

            // Move the pointer 1 spot to the right of the delimiter
            pointer = delimiter + 1;

            // Extract the word
            String word = encodedStr.substring(pointer, pointer + length);
            
            // Store the word
            decodedWords.add(word);

            // Increment the pointer
            pointer += length;
        }

        return decodedWords;
    }
}
