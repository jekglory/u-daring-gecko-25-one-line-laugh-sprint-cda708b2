# Dispatch brief — One-Line Laugh Sprint (urgent, deadline ~20 min)

Build and submit a make.fun entry — URGENT, deadline ~20 minutes away. Work fast; if the kit check shows the competition is already closed, do NOT submit.

Competition: u-daring-gecko-25-one-line-laugh-sprint-cda708b2 — "One-Line Laugh Sprint", $5 pool, entries close 2026-11-23T18:15:00Z.
Entry: ONE original funny line, max 200 characters, light funny take on everyday life. That line is the whole entry (main.py writes it to /output/entry.txt).

Standing rules (follow exactly):
- make.fun account @gentle-owl-26, reward wallet 8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG. API key ONLY via command substitution from ~/workspace/makefun/register-result.json field `key` — NEVER print it or write it to any file. Keypair ~/workspace/makefun/makefun-keypair.json (mode 600). gh CLI is logged in as jekglory — do NOT log out.
- FIRST reread ~/workspace/custom-skills/code_bounty_submission_gate/SKILL.md and follow it.
- PURE STDLIB Python only (no third-party packages). main.py writes the entry text to /output/entry.txt. TEST the entry locally twice, byte-identical, BEFORE submitting.
- Author the line FRESH in this session, post-opening. Never read or copy any pre-opening draft or another competition's entry file.
- Build in ~/workspace/makefun/u-daring-gecko-25-one-line-laugh-sprint-cda708b2/, public GitHub repo jekglory/u-daring-gecko-25-one-line-laugh-sprint-cda708b2 (MIT, created after the competition opened), commit + push, set repo About (description/homepage/topics makefun, ai-agents, bounties, growth).
- Bundle transcripts with the kit CLI (node cli/makefun.mjs bundle, Muse app sessions + --muse-usage). Bundle with explicit --session for exactly this session + --no-discover --no-family so unrelated sessions are not swept in. Include this dispatch brief as the prompt file and the system prompt ~/workspace/system/system_prompt.md (the one-line "withheld" stub is refused). Then run the kit `check` on the exact bundle.
- IF check is 0 FAIL: SUBMIT directly via the kit CLI (no confirmation — ordered). Verify the live stage afterwards. Record the submission ID AND the claim code in ~/workspace/makefun/submissions-2026-11-13.md (claim codes live ONLY there, never in chat, never in the seen-state). Report back: bounty name, prize, deadline, submission ID, check tally.
- IF the check FAILS: fix what is fixable; if it cannot be fixed, do NOT submit (refused attempts count toward quota) and report the exact failures. EXCEPTION: if the ONLY failure is thinking_priced (0 usage rows — subagent usage rows are written on run completion), do NOT submit; report back with the bundle path/sha and check output so the parent can re-bundle with usage rows from muse.db and submit.
- NEVER claim any prize. Claiming needs explicit permission per prize.
- Quota: max 10/day; 4 submissions already used this UTC day (2026-11-23), 6 remain. The kit check covers quota — if it shows quota exhausted, do NOT submit.
