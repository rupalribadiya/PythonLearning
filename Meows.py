# run on terminal using command "mypy Meows.py"

def meow(n: int) -> str:
    return "Meow\n" * n;

n: int = int(input("Enter a number: "))
meows: str = meow(n)
print(meows)