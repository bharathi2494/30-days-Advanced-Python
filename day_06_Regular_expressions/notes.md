# Regular Expressions – Python

## Overview
In Python, regular expressions (regex) are handled using the built-in `re.module`, which provides a suite of tools for **searching, matching, and manipulating text** based on specified patterns.

## 1. Character Classes
Used to match **one character from a set**.

**Examples:**
- `[a-z]` → lowercase letters  
- `[A-Z]` → uppercase letters  
- `[0-9]` → digits  
- `[^0-9]` → non-digits  

```python
re.findall(r"[A-Z][a-z]+", "Alice Bob")
```
## 2. Predefined Character Sets
| Pattern | Meaning        |
| ------- | -------------- |
| `\d`    | Digit          |
| `\w`    | Word character |
| `\s`    | Whitespace     |
| `\D`    | Non-digit      |
```python
re.findall(r"\d+", "ID 45 Cost 300")
```
## 3. Quantifiers
Control repetition.
| Quantifier | Meaning         |
| ---------- | --------------- |
| `*`        | Zero or more    |
| `+`        | One or more     |
| `?`        | Optional        |
| `{n}`      | Exactly n times |
```python
re.findall(r"\d{4}", "2023 1998")
```
## 4. Anchors
Define position in text.
| Anchor | Meaning         |
| ------ | --------------- |
| `^`    | Start of string |
| `$`    | End of string   |
| `\b`   | Word boundary   |
```python
re.match(r"^\d{10}$", "9876543210")
```
## 5. Groups and Alternation
Used to group patterns and match alternatives.
```python
(Mr|Ms|Dr)\.\s[A-Z][a-z]+
```
## 7. Regex Methods (Python)
| Method         | Description      |
| -------------- | ---------------- |
| `re.match()`   | Match from start |
| `re.search()`  | Find first match |
| `re.findall()` | Find all matches |
| `re.sub()`     | Replace text     |

## 8. Regex Flags
| Flag   | Purpose             |
| ------ | ------------------- |
| `re.I` | Ignore case         |
| `re.M` | Multiline           |
| `re.S` | Dot matches newline |

## Key Takeaways:
- Regex helps in validation and text extraction
- Quantifiers control repetition
- Anchors ensure correct position
- Groups improve pattern structure



