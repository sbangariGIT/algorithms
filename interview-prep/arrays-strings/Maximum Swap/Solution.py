class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        current_max_index = -1
        swap_a_index = None
        swap_b_index = None

        for i in range(len(num_str) - 1, -1, -1):
            if current_max_index < 0:
                current_max_index = i
                continue
            if num_str[i] < num_str[current_max_index]:
                swap_a_index = i
                swap_b_index = current_max_index
            if num_str[i] > num_str[current_max_index]:
                current_max_index = i
        if swap_a_index != None and swap_b_index != None:
            num_str[swap_a_index], num_str[swap_b_index] = (
                num_str[swap_b_index],
                num_str[swap_a_index],
            )
        return int("".join(num_str))