def translate(text: str) -> str:
    vowels = "aeiou"
    text = text.split()
    result = []

    for word in text:
        word = word.lower()

        # Rule 1
        if word[0] in vowels or word.startswith(("xr", "yt")):
            result.append(word + "ay")

        # Rule 3: "qu" ở đầu hoặc ngay sau cụm phụ âm đầu
        elif word.startswith("qu") or (word[0] not in vowels and word[1:3] == "qu"):
            pos = word.index("qu") + 2
            result.append(word[pos:] + word[:pos] + "ay")

        # Rule 4: ^[^aeiou]+y  (y không ở đầu, và không có nguyên âm trước y)
        elif "y" in word and word[0] not in vowels:
            y_pos = word.index("y")
            if y_pos > 0 and not any(ch in vowels for ch in word[:y_pos]):
                result.append(word[y_pos:] + word[:y_pos] + "ay")
            else:
                # không thoả Rule 4 -> rơi về Rule 2
                for i, ch in enumerate(word):
                    if ch in vowels:
                        result.append(word[i:] + word[:i] + "ay")
                        break
                else:
                    result.append(word + "ay")

        # Rule 2: cụm phụ âm đầu
        else:
            for i, ch in enumerate(word):
                if ch in vowels:
                    result.append(word[i:] + word[:i] + "ay")
                    break
            else:
                result.append(word + "ay")

    return " ".join(result)