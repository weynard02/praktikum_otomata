stack = []
top = -1

def push(element: str):
	global top
	top += 1
	stack[top] = element

def pop():
	global top
	element = stack[top]
	top -= 1
	return element

def isPalindrome(string: str) -> bool:
	global stack
	length = len(string)

	stack = ['0'] * (length + 1)

	mid = length // 2
	i = 0
	while i < mid:
		push(string[i])
		i += 1

	if length % 2 != 0:
		i += 1

	while i < length:
		element = pop()
		if element != string[i]:
			return False
		i += 1
		
	return True

if __name__ == "__main__":
    string = input("Enter word: ")

    if isPalindrome(string):
        print(f"{string} is a Palindrome")
    else:
        print(f"{string} is NOT a Palindrome")
