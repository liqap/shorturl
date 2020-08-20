import pyshorteners

url = str(input("Введите ссылку: "))

print(f"Усешно! Ваша ссылка: {pyshorteners.Shortener().tinyurl.short(url)}")
