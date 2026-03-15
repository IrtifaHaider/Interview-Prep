A Hash Map is a data structure that stores data in key → value pairs.
## The Core Idea
 Instead of storing items in order (like an array), a hash map uses a **hash function** to convert a key into an index, then stores the value at that index.
 
 ---
 ## How it works, step by step
 1. **You provide a key** — like `"name"`, `"age"`, or `"city"`.
2. **The hash function runs** — it does math on the key and spits out a number (an index). For example, `"name"` might become `1`, and `"age"` might become `3`.
3. **The value is stored at that index** — so `"Alice"` goes into slot 1, and `30` goes into slot 3.
4. **To look it up later** — you give the key again, the same hash function runs, you get the same index, and you go directly to that slot. No searching needed!
 
---
---
 
## The Big Deal: Speed
 
| Operation | Array (searching) | Hash Map |
|-----------|-------------------|----------|
| Find a value | O(n) — check every item | **O(1)** — jump straight there |
| Insert | O(n) | **O(1)** |
| Delete | O(n) | **O(1)** |
 
This is why hash maps are used *everywhere* — they make lookups almost instant.
 
---
## What's a collision?
 
When two different keys produce the **same index**, that's a collision. For example, both `"age"` and `"city"` might hash to bucket 3. Hash maps handle this by **chaining** — they store a small list at that bucket.
 
---
## In real code
 
```python
# Python — dictionary IS a hash map
student = {}
student["name"] = "Irtifa"   
student["age"]  = 25
 
print(student["name"])      #  (instant lookup!)
student["university"] = "JU" #  Add Data
student["age"] = 26 # Update Value

if "name" in student:  #  Check if Key Exists
    print("Exists")

for key, value in student.items():  #  Loop Through Hash Map
    print(key, value)


Output: 
name Irtifa
age 26
university JU

```
 
---
