const arr = [1, 2, 3]

// for
for (let i = 0; i < arr.length; i++) {
    console.info(arr[i])
}

// while
let j = 0
while (j < arr.length) {
    console.info(arr[j])
    j += 1
}

// for...of loop used to iterate over iterable objects like arrays, strings, sets, maps, etc.
for (const value of arr) {
    console.info(value);
}

// for...in loops through all enumerable properties of an object.
// Primarily used for objects to iterate over keys.
const obj = { one: 1, two: 2, three: 3 };

for (const key in obj) {
    if (Object.hasOwnProperty.call(obj, key)) {
        console.info(key, obj[key]);
    }
}
