from nltk.corpus import wordnet
import nltk

# Download WordNet resources (run only once)
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# Caesar Cipher Decryption Function
def caesar_decrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
        else:
            result += char
    return result

# NLP + WordNet Scoring Function
def score_text_nlp(text):
    count = 0
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 3, min(i + 9, len(text))):
            word = text[i:j]
            if wordnet.synsets(word):
                count += 1
                break
    return count

# Encrypted text (no spaces)
cipher_text = """NVVAPLOREFRPHEVGLRAUNAPRFGUERNGQRGRPGVBANHGBZNGRFERFCBAFRFNAQFGERATGURAFBIRENYYFRPHEVGLCBFGHERVGNANYLMRFINFGNZBHAGFBSQNGNVQRAGVSVRFCNGGREAFCERQVPGFCBGRAGVNYGUERNGFNAQNHGBZNGRFGNFXFYVXRYBTNANYLFVFNAQIHYARENOVYVGLFPNAAVATRANOYVATSNFGRENAQZBERRSSRPGVIRERFCBAFRFGBPLORENGGNPXF"""

best_key = None
best_score = 0
best_sentence = ""

# Try keys 1 through 25
for key in range(1, 26):
    decrypted = caesar_decrypt(cipher_text, key)
    score = score_text_nlp(decrypted)

    print(f"\n🔑 Key {key}:\n{decrypted}\n=> Score: {score}")

    if score > best_score:
        best_score = score
        best_key = key
        best_sentence = decrypted

# Final result
print("\n" + "="*60)
print(f"✅ Best Decryption:\n{best_sentence}")
print(f"🔐 Best Key: {best_key}")
print("="*60)
