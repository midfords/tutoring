/**
 * Print Iterators
 * 
 * Given an array of Iterators, return a new array containing all values in each
 * iterator. The order of the new array is all the first items in the iterators,
 * followed by all the second and so forth. If an iterator exhausts it's items, 
 * simply ignore it until all iterators are empty. *Remember iterators only have
 * next():int and hasNext():boolean methods.
 * 
 * Example: [Iterator(1,4,2,5), Iterator(3,2), Iterator(5,6,4,7,5)]
 *   -> [1,3,5,4,2,6,2,4,5,7,5]
 * Explanation: Each of the first items is removed from the list of iterators (1,3,5), 
 * followed by each of the second items (4,2,6), followed by the third (2,4) and so forth.
 */
