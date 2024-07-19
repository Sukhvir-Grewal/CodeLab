#include <iostream>
#include <vector>

std::vector<int> twoSum(const std::vector<int> &nums, int target) {
  std::vector<int> newarr;
  for (int i = 0; i < nums.size(); i++) {
    for (int j = i + 1; j < nums.size(); j++) {
      if ((nums[i] + nums[j]) == target) {
        newarr.push_back(i);
        newarr.push_back(j);
        return newarr;
      }
    }
  }
  return newarr;
}

int main(){
    std::vector<int> arr = {2, 7, 11, 15};
    std::vector<int> result = twoSum(arr, 9);
    if (!result.empty()) {
        std::cout << "Indices: " << result[0] << ", " << result[1] << std::endl;
    } else {
        std::cout << "No two sum solution found." << std::endl;
    }
    return 0;
}
