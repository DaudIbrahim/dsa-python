function isPalindrome(inputString: string): boolean {
    // Convert to lowercase
    const lowercaseString = inputString.toLowerCase();

    // Remove non-alphanumeric characters using a regular expression
    const alphanumericString = lowercaseString.replace(/[^a-z0-9]/g, '');

    let left = 0
    let right = (alphanumericString.length - 1)

    while (left <= right) {
        if (alphanumericString.charAt(left) !== alphanumericString.charAt(right)) {
            return false
        }

        left += 1
        right -= 1
    }

    return true;
};