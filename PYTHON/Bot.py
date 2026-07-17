def trap(height):
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax = rightMax = 0
    res = 0

    while l < r:
        if height[l] < height[r]:
            if height[l] >= leftMax:
                leftMax = height[l]
            else:
                res += leftMax - height[l]
            l += 1
        else:
            if height[r] >= rightMax:
                rightMax = height[r]
            else:
                res += rightMax - height[r]
            r -= 1
vhj
    return res
// print the return values 