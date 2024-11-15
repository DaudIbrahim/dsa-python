/**
 * Array
 */
const arr = [1]
arr.push(2)
arr.push(3)

console.info('Array', arr)

/**
 * Set
 */
const set = new Set([1])
set.add(2)
set.add(3)

console.info('Set', [...set.values()])

/**
 * Object
 * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties
 */
const obj = { one: 1 }
obj['two'] = 2
obj['three'] = 3

console.info('Object Keys', [...Object.keys(obj)])
console.info('Object Values', [...Object.values(obj)])

for (const key in obj) {
    if (Object.hasOwnProperty.call(obj, key)) {
        const element = obj[key];
        console.info(element)
    }
}

const values = Object.values(obj)
console.info(values[0])

/**
 * Map
 */
const map = new Map([['one', 1]])
map.set('two', 2)
map.set('three', 3)

console.info('Map Keys', [...map.keys()])
console.info('Map Values', [...map.values()])

/**
 * Iterators and the for...of Loop
 * https://github.com/DaudIbrahim/knowledge-base-pvt/blob/main/concepts/js/iterators-and-generators-in-js.md#understanding-iterators-and-generators-in-javascript
 */
// Set.prototype.values() and Map.prototype.values() return iterators.
const setIterator = set.values();
const mapIterator = map.values();

// You can loop through iterators using the for...of loop.
for (const value of setIterator) {
    console.log('Set value:', value); // Logs 1, 2, 3
}

for (const value of mapIterator) {
    console.log('Map value:', value); // Logs 1, 2, 3
}

// Arrays are also iterable, so you can use for...of with them as well.
for (const value of arr) {
    console.log('Array value:', value); // Logs 1, 2, 3
}
