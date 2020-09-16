phone_num = "       (555) 123-4567    "
print("phone_num with whitespace: " + phone_num)

phone_num = "       (555) 123-4567    ".strip()
print("Fixed phone num: " + phone_num)

phone_num = "       (555) 123-4567"
print("Space just on left side: " + phone_num)
print("Space on left side fixed: " + phone_num.lstrip())

phone_num = "(555) 123-4567      "
print("Space just on right side: " + phone_num)
print("Space on right side fixed: " + phone_num.rstrip())
