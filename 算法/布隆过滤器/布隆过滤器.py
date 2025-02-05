import hashlib


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate a list of hash values for the given item."""
        result = []
        for i in range(self.hash_count):
            hash_value = int(hashlib.sha256((str(item) + str(i)).encode()).hexdigest(), 16)
            result.append(hash_value % self.size)
        return result

    def add(self, item):
        """Add an item to the bloom filter."""
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        """Check if an item is in the bloom filter."""
        for hash_value in self._hashes(item):
            if self.bit_array[hash_value] == 0:
                return False
        return True


# 示例用法
bf = BloomFilter(size=100, hash_count=3)
bf.add("apple")
bf.add("banana")

print(bf.check("apple"))  # 输出: True
print(bf.check("banana"))  # 输出: True
print(bf.check("orange"))  # 输出: False (可能会有误判)
