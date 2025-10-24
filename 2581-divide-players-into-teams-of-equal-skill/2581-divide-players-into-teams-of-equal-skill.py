class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        no_of_teams = len(skill) / 2
        total_skill = sum(skill)
        if total_skill%no_of_teams != 0:
            return -1
        team_skill = total_skill / no_of_teams
        skill_dict = defaultdict(int)
        chemistry = 0

        for player_skill in skill:
            complementary_skill = team_skill - player_skill
            if complementary_skill in skill_dict:
                chemistry += complementary_skill * player_skill
                skill_dict[complementary_skill] -= 1
                if skill_dict[complementary_skill] == 0:
                    del skill_dict[complementary_skill]
            else:
                skill_dict[player_skill] += 1
        if len(skill_dict) != 0:
            return -1
        return int(chemistry)