/// <reference types="node" />
// teams/builder.ts
//
//  Generate a *packed* team string that poke-env (and Showdown) can consume.
//  Usage:   node teams/builder.ts            → prints one gen9randombattle team
//           node teams/builder.ts gen8randombattle  → prints a Gen 8 team
//  Import:  const {buildPackedTeam} = require('./teams/builder');

import {TeamGenerators} from '@pkmn/randoms';
import {Team} from '@pkmn/sets';

/** Build one packed team string for the requested ladder format. */
export function buildPackedTeam(
  format = 'gen9randombattle',
  seed?: number[],             
): string {
  const prng = seed ? seed.join(',') as `${number},${string}` : undefined;
  const gen  = TeamGenerators.getTeamGenerator(format, prng);
  return new Team(gen.getTeam()).pack();
}

/* ── CLI runner ─────────────────────────────────────────────────────────────── */
if (require.main === module) {
  const fmt = process.argv[2] ?? 'gen9randombattle';
  console.log(buildPackedTeam(fmt));
}
