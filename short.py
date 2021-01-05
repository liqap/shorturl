import pyfiglet
from colorama import init, Fore
import pyshorteners

banner = pyfiglet.figlet_format("shorturl")
print(Fore.GREEN + banner)
print("Автор: @neo0089")

url = str(input("Введите ссылку: "))

print(f"Усешно! Ваша ссылка: {pyshorteners.Shortener().tinyurl.short(url)}")
