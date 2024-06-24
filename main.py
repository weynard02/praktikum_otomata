stack = []

def push(element: str):
	stack.append(element)

def pop():
    return stack.pop()

def isPalindrome(string: str) -> bool:
	global stack
	length = len(string)

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
