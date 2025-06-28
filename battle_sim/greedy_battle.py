# battle_sim/greedy_battle.py

import subprocess, asyncio

from poke_env.teambuilder import ConstantTeambuilder
from battle_classes import MaxDamagePlayer

# Running some TypeScript code to build teams.
# Probably not ideal for performance long term.
NODE_CMD = ["npx", "tsx", "teams/builder.ts"]


def build_team(format_: str = "gen9randombattle") -> str:
    """Return a packed Showdown team string produced by the TS generator."""
    packed = subprocess.check_output(NODE_CMD + [format_], text=True).strip()
    if not packed:
        raise RuntimeError("team generator returned empty string")
    return packed

def main():
    team1 = ConstantTeambuilder(build_team())     # bot A
    team2 = ConstantTeambuilder(build_team())     # bot B

    print(team1.team)
    print(team2.team)
    p1 = MaxDamagePlayer(battle_format="gen9randombattle", team=team1)
    p2 = MaxDamagePlayer(battle_format="gen9randombattle", team=team2)
    print(p1._team)
    # await p1.battle_against(p2, n_battles=1)
    # print("p1 win rate:", p1.win_rate)




if __name__ == "__main__":
    main()