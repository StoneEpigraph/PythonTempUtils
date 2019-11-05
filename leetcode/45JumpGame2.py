def jump(nums) -> int:
    total_len = len(nums)
    print("total_len: " + str(total_len))
    this_total_value = nums[0]
    this_num = 0
    jump_count = 0
    if total_len == 1:
        return 0
    if total_len == 2:
        return 1
    if this_total_value + 1 >= total_len:
        return 1
    while this_num < total_len:
        this_value = nums[this_num]
        temp_this_total_value = this_total_value
        temp_jump = 1
        print("this_value: " + str(this_value))
        for i in range(1, this_value + 1):
            print("this_num: " + str(this_num))
            if this_num + i + 1 < total_len and this_total_value + nums[this_num + i + 1] >= temp_this_total_value:
                temp_this_total_value = this_total_value + nums[this_num + i + 1]
                temp_jump = i + 1
        print("this_num: " + str(this_num))
        print("this_total_value: " + str(this_total_value))
        print("temp_jump: " + str(temp_jump))
        this_num = this_num + temp_jump
        print("temp_this_total_value: " + str(temp_this_total_value))
        this_total_value = temp_this_total_value
        jump_count = jump_count + 1
        print("jump_count: " + str(jump_count))
        print('*' * 50)
        if this_total_value + 1 >= total_len:
            print("jump")
            return jump_count
    print(jump_count)
    return jump_count


if __name__ == '__main__':
    arr = [2, 3, 1, 1, 4]
    # arr = [1, 2, 3]
    # arr = [1, 3, 2]
    # arr = [3, 2, 1]
    # arr = [1, 1, 1, 1]
    # arr = [1, 2, 0, 1]
    arr = [1,1,1,2,1]
    jump_counts = jump(arr)
    print(jump_counts)

