# VARIANT.md — Variant C: The Nightly Seed-Word Count

## Concept
The wallet treats 3 AM as sacred. Every night at 3 AM it performs its own
private bedtime ritual: counting its twelve seed words, in order, twice —
like a shepherd counting sheep, or a guard doing roll-call. Your transaction
arrives mid-count, makes it lose its place, and it has to start over from
one. The refusal *is* the ritual: it will not sign until the count is done,
i.e. come back at dawn. The 3 AM hour is load-bearing — the count happens at
3 AM and at no other hour; swap in 3 PM and the line collapses. No battery,
firmware-update, or cold-storage jokes anywhere in this variant.

## Versions (one concept, iterated v1 → v8)

| Ver | Chars | Line |
|-----|-------|------|
| v1 | 134 | It's 3 AM — my nightly seed-word count. Twelve words, in order, twice. Your transaction just made me lose count, and now I start over. |
| v2 | 121 | 3 AM is when I count my seed words — twelve, in order, twice — and your transaction just made me lose count. Back to one. |
| v3 | 124 | At 3 AM I count my seed words: twelve, in order, twice. Your transaction made me lose count. Back to one. Come back at dawn. |
| v4 | 112 | I count my seed words at 3 AM — twelve, in order, twice. You made me lose count. Back to one. Come back at dawn. |
| v5 | 123 | 3 AM is seed-word o'clock: twelve words, in order, twice. Your transaction made me lose count. Back to one. Try me at dawn. |
| v6 | 124 | Every night at 3 AM I count my seed words — twelve, in order, twice. You made me lose count. Back to one. Come back at dawn. |
| v7 | 132 | At 3 AM I count my seed words to sleep — twelve, in order, twice. Your transaction woke me at seven. Back to one. Come back at dawn. |
| v8 | **117** | **3 AM is when I count my seed words — twelve, in order, twice. You made me lose count. Back to one. Come back at dawn.** |

## Why each earlier version lost
- **v1** — "just" is filler; "and now I start over" trails off instead of landing; no refusal, only a complaint.
- **v2** — "Back to one" is the right punch, but the line ends without the refusal — it never says it won't sign.
- **v3** — the colon stalls the opening; "At 3 AM I count" buries the hour in a prepositional phrase instead of making it the subject.
- **v4** — tightest of the set, but it opens with "I count" and the hour arrives as an afterthought; the ritual should be announced by the hour.
- **v5** — "seed-word o'clock" is a gimmick that spends the joke on a coinage; "Try me at dawn" is a dare, not a refusal.
- **v6** — "Every night" adds the ritual feel, but "Every night at 3 AM I count" is three soft words before the sentence starts working; the hour should lead.
- **v7** — "woke me at seven" tries to be clever twice (seventh word / 7 AM) and lands as neither; the reader has to solve it instead of laughing at it.

## Shipped: v8 (117 characters)
> 3 AM is when I count my seed words — twelve, in order, twice. You made me lose count. Back to one. Come back at dawn.

**Why it won:** the hour leads and owns the sentence; the ritual is concrete
(twelve words, in order, twice); "Back to one" is the device resetting
itself — the punch; "Come back at dawn" is the refusal. No word is spare.
Device voice throughout: a wallet with a private nightly ritual and a grudge
against whoever interrupts it.
