# GenLayer Intelligent DAO Grant Evaluator

An on-chain Intelligent Contract built for the GenLayer protocol that automates DAO grant evaluations using decentralized LLM consensus.

## Overview
Traditional DAOs struggle with slow, subjective, and manual review processes for funding proposals. This contract establishes an objective, transparent, and autonomous evaluation mechanism running directly on GenLayer's Optimistic Democracy consensus.

## Features
- **Decentralized LLM Evaluation:** Executes multi-validator LLM consensus via `gl.nondet.exec_prompt` and `gl.eq_principle.strict_eq`.
- **Structured Scoring:** Rates proposals across feasibility, ecosystem alignment, and budget realism.
- **Native GenVM Storage:** Stores immutable evaluations using GenLayer's `TreeMap` and `u32` primitive types.

## Contract Functions
- `submit_and_evaluate_proposal()`: Public write function that accepts proposal details, generates consensus prompt, and records structured verdicts.
- `get_evaluation()`: View function returning the full evaluation metrics and verdict.
- `get_total_proposals()`: View function returning the historical proposal volume.

## Deployment Details
- **Network:** GenLayer Testnet
- **Contract Address:** `0x3dcC6F819Bb7bB6D75fFFC92DB101BdC82B3cAc9`
- **Runtime:** Python (GenVM)
- **Status:** Finalized
