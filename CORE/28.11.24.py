# 1. Кожне друге число
def every_second(nums):
    return nums[1::2]

# 2. Видалення парних елементів (залишаються непарні)
def remove_evens(nums):
    return [x for x in nums if x % 2 != 0]

# 3. Список слів у зворотному порядку
def reverse_words(words):
    return words[::-1]

# 4. Елементи менші за середнє значення
def smaller_than_avg(nums):
    if not nums:
        return []
    avg = sum(nums) / len(nums)
    return [x for x in nums if x < avg]

# Тести
print("Кожне друге:", every_second([10, 20, 30, 40, 50]))
print("Без парних:", remove_evens([1, 2, 3, 4, 5, 6]))
print("Зворотні слова:", reverse_words(["код", "це", "біль"]))
print("Менші за середнє:", smaller_than_avg([1, 2, 10, 20, 30]))