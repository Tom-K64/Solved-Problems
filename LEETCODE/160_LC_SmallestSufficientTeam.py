"""
Problem Link:
https://leetcode.com/problems/smallest-sufficient-team/
"""

class Solution:
    def smallestSufficientTeam(self, req_skills,people):
        len_people,len_req_skills = len(people),len(req_skills)
        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * len_people
        for i in range(len_people):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]
        dp = [(1 << len_people) - 1] * (1 << len_req_skills)
        dp[0] = 0
        for skills_mask in range(1, 1 << len_req_skills):
            for i in range(len_people):
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if smaller_skills_mask != skills_mask:
                    people_mask = dp[smaller_skills_mask] | (1 << i)
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        answer_mask = dp[(1 << len_req_skills) - 1]
        answer = []
        for i in range(len_people):
            if (answer_mask >> i) & 1:
                answer.append(i)
        return answer
