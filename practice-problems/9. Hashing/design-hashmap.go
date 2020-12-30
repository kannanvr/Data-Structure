package ___Hashing

//implement hash map by creating your own hashTable, if range is known.
type MyHashMap struct {
	hashTable [1000000]int
}


/** Initialize your data structure here. */
func Constructor() MyHashMap {
	myMap:=MyHashMap{}
	for i,_:=range myMap.hashTable {
		myMap.hashTable[i]=-1
	}
	return myMap
}


/** value will always be non-negative. */
func (this *MyHashMap) Put(key int, value int)  {
	this.hashTable[key]=value
}


/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
	return this.hashTable[key]
}


/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int)  {
	this.hashTable[key]=-1
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */


//drawbacks of using hashtable
/*
1. only supported for small key-range, not suitable for integers like phone numbers.
2. not suitable for floating point numbers or any string key, bcz array index can't be floating or string.

to overcome these problems use hash functions ie takes large input and convert to small key that can be use as array index.
Example of good hash function
a) it should be uniformly distributed.
b) take size of hashtable as prime number bcz it has less factor and so that will get more uniform distribution.

*/
