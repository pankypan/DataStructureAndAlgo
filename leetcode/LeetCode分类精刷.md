# LeetCode分类精刷

## String



## LinkedList



## Array



## StackAndQueue



## HashTable



## Tree



## BinarySearchTree



## Heap

```python
# 253, 624
```

### [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

#### 题目

![image-20210527222751738](assets/image-20210527222751738.png)

#### 解题思路

**优先队列**

优先队列的思路是很朴素的。因为第 `K` 大元素，其实就是整个数组排序以后后半部分最小的那个元素。因此，我们可以维护一个有 `K` 个元素的最小堆：

1. 如果当前堆不满，直接添加；
2. 堆满的时候，如果新读到的数小于等于堆顶，肯定不是我们要找的元素，只有新都到的数大于堆顶的时候，才将堆顶拿出，然后放入新读到的数，进而让堆自己去调整内部结构。



#### code

```python
import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        """
        Heap
            使用容量为 k 的小顶堆
            元素个数小于 k 的时候，放进去就是了
            元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换
        """
        priority_queue = list()

        for i in range(k):
            heapq.heappush(priority_queue, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > priority_queue[0]:
                heapq.heapreplace(priority_queue, nums[i])
        return priority_queue[0]
```





### [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

#### 题目

![image-20210527223819932](assets/image-20210527223819932.png)

#### 解题思路

**最小堆**

题目最终需要返回的是前 k*k* 个频率最大的元素，可以想到借助堆这种数据结构，对于 k*k* 频率之后的元素不用再去处理，进一步优化时间复杂度。

![2b27b1db106a53abe239c5be8e49a800522ab2f6637940cb556bcfe1232ff333-file_1561712388055](assets/2b27b1db106a53abe239c5be8e49a800522ab2f6637940cb556bcfe1232ff333-file_1561712388055.jpg)

具体操作为：

- 借助 **哈希表** 来建立数字和其出现次数的映射，遍历一遍数组统计元素的频率
- 维护一个元素数目为 *k* 的最小堆
- 每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
- 如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
- 最终，堆中的 *k* 个元素即为前 *k* 个高频元素



#### code

```python

```





### [373. 查找和最小的K对数字](https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/)

#### 题目

![image-20210527225041866](assets/image-20210527225041866.png)

#### 解题思路

**优先队列**

- 它仅从矩阵左上角的第一对开始，然后根据需要从那里开始扩展。 
- 每当将一对选择为输出结果时，该行中的下一对就会添加到当前选项的优先队列中。 
- 同样，如果所选对是该行中的第一对，则将下一行中的第一对添加到队列中。

![cba00e2cb2cf8a1158aa8caff0c42259a0263bbb5e623e99c2280da21bdd875d-组合2](assets/cba00e2cb2cf8a1158aa8caff0c42259a0263bbb5e623e99c2280da21bdd875d-组合2.png)

#### code

```python

```



## Graph



## BitOperation



## DFS

```python
# 98, 113, 394, 547, 1273
```



## BFS

```python
# 102, 207, 301, 934
```



## IterationAndRecursion

```python
# 94, 144, 145, 230, 247, 544, 625, 687
```



## Sort

```python
# 56, 147, 220, 252
```



## BinarySearch



## DivideAndConquer

```python
# 4, 23, 53, 215, 240, 327
```



## Backtracking

```python
# 10, 17, 22, 39, 46(classical), 1239
```



## Greedy

```python
# 253, 406, 621
```



## DP

```python
# 5(classical), 10, 300, 647
```















































