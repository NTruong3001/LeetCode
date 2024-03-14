class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        # Duyệt qua mảng nums và lưu trữ giá trị của mỗi phần tử và chỉ số của nó trong num_indices
        for i, num in enumerate(nums):
            num_indices[num] = i

        # Duyệt qua mảng nums một lần nữa
        for i, num in enumerate(nums):
            diff = target - num
            # Kiểm tra nếu diff đã tồn tại trong num_indices và không trùng với chỉ số hiện tại
            if diff in num_indices and num_indices[diff] != i:
                # Trả về chỉ số của hai phần tử có tổng bằng target
                return [i, num_indices[diff]]