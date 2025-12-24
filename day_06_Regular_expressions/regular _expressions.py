import re

# 1.Email Validation
emails = [
    "user@gmail.com",
    "user.name@company.in",
    "admin@domain",
    "test_user@domain.co",
    "invalid-email.com",
    "john.doe@website.org"
]
pattern=r"^[a-zA-Z0-9._]+\.[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

correct_emails=[]

for email in emails:
    if re.search(pattern, email):
        correct_emails.append(email)

print(correct_emails)

# 2.Phone Number Validation
phone_numbers = [
    "9876543210",
    "1234567890",
    "12345",
    "98765432101",
    "9998887776"
]

pattern1=r"^\d{10}$"
correct_mobNos=[]
for number in phone_numbers:
    if re.search(pattern1, number):
        correct_mobNos.append(number)
print(correct_mobNos)

# 3.Username Validation
usernames = [
    "user_01",
    "1user",
    "admin123",
    "guest",
    "my_name",
    "_invalid"
]
pattern=r"^[a-zA-Z]\w{5,15}$"

user_name=[]

for name in usernames:
    if re.fullmatch(pattern, name):
        user_name.append(name)
print(user_name)

# 4.Extract Numbers from Text
texts_with_numbers = [
    "Order 25 items for 300 rupees",
    "Invoice #12345 paid on 2025-12-24",
    "Room 101 has 2 beds",
    "No numbers here"
]

pattern=r"\d+"
exact_nos=[]

for text in texts_with_numbers:
    result=re.findall(pattern, text)
    exact_nos.extend(result)

print(exact_nos)

# 5.Extract Capitalized Words
capitalized_texts = [
    "Python Is Easy To Learn",
    "Hello World From OpenAI",
    "this sentence has no caps",
    "Data Science and AI"
]

pattern=r"[A-Z]"
capital_letters=[]
for text in capitalized_texts:
    result= re.findall(pattern, text)
    capital_letters.extend(result)

print(capital_letters)

# 6.Extract File Extensions
file_names = [
    "data.csv",
    "image.png",
    "notes.txt",
    "archive.zip",
    "report.pdf"
]
pattern=r"\.[a-z]+$"
file_extensions=[]
for file in file_names:
    result= re.findall(pattern, file)
    file_extensions.extend(result)
print(file_extensions)

#7.Mask Digits(replace digits with *)
texts_with_digits = [
    "Card number 1234",
    "My phone 9876543210",
    "Invoice 2025"
]
pattern=r"\d"
masked=[]

for str in texts_with_digits:
    result=re.sub(pattern, "*", str)
    masked.append(result)
print(masked)

# 8.Remove Extra Spaces
texts_with_spaces = [
    "Python    is     powerful",
    "This   is   a    test",
    "Multiple       spaces here"
]
clean_text=[]

for text in texts_with_spaces:
    cleaned=re.sub(r"\s+", " ", text).strip()
    clean_text.append(cleaned)
    
print(clean_text)

