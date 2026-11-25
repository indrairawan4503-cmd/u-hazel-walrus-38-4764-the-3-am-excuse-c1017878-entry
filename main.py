"""The 3 AM Excuse — Variant C: THE NIGHTLY SEED-WORD COUNT.

Concept: the wallet treats 3 AM as sacred. Every night at 3 AM it performs
its own private bedtime ritual — counting its twelve seed words, in order,
twice, like a shepherd counting sheep (or a guard doing roll-call). Your
transaction arrives mid-count, makes it lose its place, and it has to start
over from one. The refusal is the ritual: it will not sign until the count
is done, i.e. come back at dawn. The 3 AM hour is load-bearing — the count
happens at 3 AM and at no other hour; swap in 3 PM and the line collapses.

Iteration history (one concept, v1-v8; only the winner ships):
  v1 (134c): "It's 3 AM — my nightly seed-word count. Twelve words, in order,
              twice. Your transaction just made me lose count, and now I
              start over."
              LOST: "just" is filler; "and now I start over" trails off
              instead of landing; no refusal, only a complaint.
  v2 (121c): "3 AM is when I count my seed words — twelve, in order, twice
              — and your transaction just made me lose count. Back to one."
              LOST: "Back to one" is the right punch, but the line ends
              without the refusal — it never says it won't sign.
  v3 (124c): "At 3 AM I count my seed words: twelve, in order, twice. Your
              transaction made me lose count. Back to one. Come back at
              dawn."
              LOST: the colon stalls the opening; "At 3 AM I count" buries
              the hour in a prepositional phrase instead of making it the
              subject of the sentence.
  v4 (112c): "I count my seed words at 3 AM — twelve, in order, twice. You
              made me lose count. Back to one. Come back at dawn."
              LOST: tightest of the set, but it opens with "I count" and
              the hour arrives as an afterthought; the ritual should be
              announced by the hour, not the other way round.
  v5 (123c): "3 AM is seed-word o'clock: twelve words, in order, twice.
              Your transaction made me lose count. Back to one. Try me at
              dawn."
              LOST: "seed-word o'clock" is a gimmick that spends the joke
              on a coinage; "Try me at dawn" is a dare, not a refusal.
  v6 (124c): "Every night at 3 AM I count my seed words — twelve, in
              order, twice. You made me lose count. Back to one. Come
              back at dawn."
              LOST: "Every night" adds the ritual feel, but "Every night
              at 3 AM I count" is three soft words before the sentence
              starts working; the hour should lead.
  v7 (132c): "At 3 AM I count my seed words to sleep — twelve, in order,
              twice. Your transaction woke me at seven. Back to one.
              Come back at dawn."
              LOST: "woke me at seven" tries to be clever twice (seventh
              word / 7 AM) and lands as neither; the reader has to solve
              it instead of laughing at it.
  v8 (117c) SHIPPED: "3 AM is when I count my seed words — twelve, in
              order, twice. You made me lose count. Back to one. Come
              back at dawn."
              WON: the hour leads and owns the sentence; the ritual is
              concrete (twelve words, in order, twice); "Back to one"
              is the device resetting itself — the punch; "Come back at
              dawn" is the refusal. No word is spare.
"""

import os

LINE = (
    "3 AM is when I count my seed words \u2014 twelve, in order, twice. "
    "You made me lose count. Back to one. Come back at dawn."
)


def main():
    data = LINE.encode("utf-8")
    # Write /output FIRST: the grader reads this copy.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Repo-root copy for local inspection; the grader sandbox is read-only,
    # so a failure here must never crash the run (exit code 1 = rejection).
    try:
        with open("entry.txt", "wb") as f:
            f.write(data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
