def max_attendees(personid):
    preferred = {i: personid[i-1] for i in range(1, len(personid)+1)}
    visited = set()
    max_count = 0
    for i in range(1, len(personid)+1):
        if i not in visited:
            count = 0
            curr = i
            while curr not in visited:
                visited.add(curr)
                count += 1
                curr = preferred[curr]
            max_count = max(max_count, count)
    return max_count // 2 if max_count % 2 == 0 else (max_count + 1) // 2


print(max_attendees([3, 4, 1, 5, 6, 7, 2]))