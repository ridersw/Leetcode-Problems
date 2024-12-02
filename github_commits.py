import subprocess
from datetime import datetime, timedelta
import sys
import os
import random
from typing import List, Dict

class DSAProblemGenerator:
    def __init__(self):
        self.problems = [
            {
                'name': 'two_sum',
                'difficulty': 'Easy',
                'template': '''
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and a target, return indices of two numbers that add up to target.
    
    Time complexity: O(n)
    Space complexity: O(n)
    
    Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()
'''
            },
            {
                'name': 'max_subarray',
                'difficulty': 'Medium',
                'template': '''
from typing import List

def max_subarray(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest sum.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Example:
    >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    6  # [4,-1,2,1] has the largest sum = 6
    """
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def test_max_subarray():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-1]) == -1
    assert max_subarray([-2,-1]) == -1
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_subarray()
'''
            },
            {
                'name': 'rotate_array',
                'difficulty': 'Medium',
                'template': '''
from typing import List

def rotate_array(nums: List[int], k: int) -> None:
    """
    Rotate array to the right by k steps in-place.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Example:
    >>> nums = [1,2,3,4,5,6,7]
    >>> rotate_array(nums, 3)
    >>> nums
    [5,6,7,1,2,3,4]
    """
    def reverse(nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    n = len(nums)
    k = k % n
    
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)

def test_rotate_array():
    nums1 = [1,2,3,4,5,6,7]
    rotate_array(nums1, 3)
    assert nums1 == [5,6,7,1,2,3,4]
    
    nums2 = [-1,-100,3,99]
    rotate_array(nums2, 2)
    assert nums2 == [3,99,-1,-100]
    print("All test cases passed!")

if __name__ == "__main__":
    test_rotate_array()
'''
            },
            {
                'name': 'merge_sorted_arrays',
                'difficulty': 'Easy',
                'template': '''
from typing import List

def merge_sorted_arrays(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge nums2 into nums1 as one sorted array in-place.
    nums1 has enough space at the end to hold nums2.
    
    Time complexity: O(m + n)
    Space complexity: O(1)
    
    Example:
    >>> nums1 = [1,2,3,0,0,0], m = 3
    >>> nums2 = [2,5,6], n = 3
    >>> merge_sorted_arrays(nums1, m, nums2, n)
    >>> nums1
    [1,2,2,3,5,6]
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

def test_merge_sorted_arrays():
    nums1 = [1,2,3,0,0,0]
    merge_sorted_arrays(nums1, 3, [2,5,6], 3)
    assert nums1 == [1,2,2,3,5,6]
    
    nums2 = [1]
    merge_sorted_arrays(nums2, 1, [], 0)
    assert nums2 == [1]
    print("All test cases passed!")

if __name__ == "__main__":
    test_merge_sorted_arrays()
'''
            },
            {
                'name': 'container_with_most_water',
                'difficulty': 'Medium',
                'template': '''
from typing import List

def max_area(height: List[int]) -> int:
    """
    Find two lines that together with x-axis forms a container that contains the most water.
    
    Time complexity: O(n)
    Space complexity: O(1)
    
    Example:
    >>> max_area([1,8,6,2,5,4,8,3,7])
    49  # 8 and 7 form a container with area = min(8,7) * 7 = 49
    """
    max_water = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        width = right - left
        max_water = max(max_water, width * min(height[left], height[right]))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

def test_max_area():
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert max_area([1,1]) == 1
    assert max_area([4,3,2,1,4]) == 16
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_area()
'''
            }
        ]

    def generate_problem(self):
        """Returns a random DSA problem"""
        problem = random.choice(self.problems)
        return problem['name'], problem['template']

class CommitPatternEnforcer:
    def __init__(self, repo_path: str, required_commits: Dict[int, int]):
        self.repo_path = repo_path
        self.required_commits = required_commits
        self.dsa_generator = DSAProblemGenerator()

    def count_commits_on_date(self, date: datetime) -> int:
        """Count commits on a specific date"""
        try:
            git_command = [
                'git',
                '-C',
                self.repo_path,
                'log',
                '--after',
                f"{date.strftime('%Y-%m-%d')} 00:00:00",
                '--before',
                f"{date.strftime('%Y-%m-%d')} 23:59:59",
                '--format=%H'
            ]
            
            result = subprocess.run(
                git_command,
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = result.stdout.strip().split('\n')
            return len([c for c in commits if c])
            
        except subprocess.CalledProcessError as e:
            print(f"Error checking commits for {date}: {str(e)}")
            return 0

    def create_and_push_dsa_problem(self, date: datetime) -> bool:
        """Create and push a new DSA problem"""
        try:
            # Generate problem
            problem_name, problem_code = self.dsa_generator.generate_problem()
            
            # Create file
            file_name = f"dsa_{problem_name}_{date.strftime('%Y%m%d')}.py"
            file_path = os.path.join(self.repo_path, file_name)
            
            with open(file_path, 'w') as f:
                f.write(problem_code)
            
            # Git operations
            subprocess.run(['git', '-C', self.repo_path, 'add', file_path], check=True)
            commit_message = f"Add {problem_name} problem for {date.strftime('%Y-%m-%d')}"
            subprocess.run(['git', '-C', self.repo_path, 'commit', '-m', commit_message], check=True)
            subprocess.run(['git', '-C', self.repo_path, 'push'], check=True)
            
            print(f"Successfully created and pushed {file_name}")
            return True
            
        except Exception as e:
            print(f"Error creating/pushing DSA problem: {str(e)}")
            return False

    def check_and_enforce_pattern(self) -> None:
        """Check commit pattern for the last month and enforce if needed"""
        today = datetime.now()
        
        print("\nStarting commit pattern check and enforcement...")
        print(f"Repository path: {self.repo_path}")
        print("Required commits per day:")
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day_num, commits in self.required_commits.items():
            print(f"{days[day_num]}: {commits} commits")
        
        # Check last 30 days
        for i in range(30):
            date = today - timedelta(days=i)
            weekday = date.weekday()  # Monday is 0, Sunday is 6
            
            # Skip Sunday (we don't have requirements for Sunday)
            if weekday == 6:
                continue
                
            required = self.required_commits.get(weekday, 0)
            actual = self.count_commits_on_date(date)
            
            print(f"\nChecking {date.strftime('%Y-%m-%d')} ({days[weekday]})")
            print(f"Required commits: {required}")
            print(f"Actual commits: {actual}")
            
            if actual < required:
                print(f"Need {required - actual} more commits")
                for _ in range(required - actual):
                    if not self.create_and_push_dsa_problem(date):
                        print("Failed to create/push problem, moving to next day")
                        break
            else:
                print("✓ Requirement met")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <repository_path>")
        return

    repo_path = sys.argv[1]
    
    # Required commits per weekday (Monday = 0, Sunday = 6)
    required_commits = {
        0: 1,  # Monday
        1: 2,  # Tuesday
        2: 3,  # Wednesday
        3: 4,  # Thursday
        4: 5,  # Friday
        5: 6,  # Saturday
    }
    
    enforcer = CommitPatternEnforcer(repo_path, required_commits)
    enforcer.check_and_enforce_pattern()

if __name__ == "__main__":
    main()