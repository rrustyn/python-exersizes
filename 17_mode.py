def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    unique_numbers = set(nums)

    common = 0

    for num in unique_numbers:
        if nums.count(num) > common:
            common = num
    return common
