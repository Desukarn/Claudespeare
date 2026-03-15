# Plot Hole Prevention & Consistency Tracking

## Overview

Based on common writer errors and the need for rigorous consistency, this supplementary guide provides systems for preventing plot holes, tracking character knowledge, and maintaining timeline integrity.

**Purpose**: Catch the "obvious" things that get missed - characters knowing information they shouldn't, timeline inconsistencies, magic rule violations, and worldbuilding contradictions.

## PART 1: CHARACTER KNOWLEDGE TRACKING

### The Problem

**Common Plot Hole**: Character A knows something they couldn't possibly know because:
- They weren't present when it was revealed
- It happened before they were introduced
- Another character never told them
- They have no way to discover it

**Example Failures**:
- Character mentions detail from scene they weren't in
- Character knows villain's plan without investigation
- Character uses information from future timeline
- Character aware of secret no one told them

### The Solution: Knowledge Matrix

**Create a tracking sheet**:

```
STORY BEAT | REVEALED INFO | WHO LEARNS IT | HOW THEY LEARN IT | WHEN
-----------|---------------|---------------|-------------------|------
Ch 3: Guard mentions password | Password is "moonrise" | Guard, Protagonist (overhears) | Eavesdropping | Ch 3, pg 47
Ch 5: Villain monologues | Plan to poison water | Villain, Henchman | Direct conversation | Ch 5, pg 89
Ch 7: Note found | Poison is in warehouse | Protagonist | Found note | Ch 7, pg 134
```

**Before ANY scene, check**:
- What does THIS character know at THIS point?
- How did they learn it?
- Can they reasonably make this deduction?

### Knowledge Categories

**DIRECT KNOWLEDGE**: Character was present, saw/heard it themselves
- Mark: ✓ (witnessed)

**INDIRECT KNOWLEDGE**: Character was told by someone who knows
- Mark: → (from [character name])

**DEDUCED KNOWLEDGE**: Character figured it out from evidence
- Mark: ? (deduced from [evidence])

**UNKNOWN**: Character doesn't know this yet
- Mark: ✗ (doesn't know)

### Character Knowledge Sheet Template

```
CHARACTER: _______________

KNOWLEDGE ITEM | STATUS | SOURCE | WHEN LEARNED
---------------|--------|--------|-------------
Villain's identity | ✗ | N/A | Not yet
Secret passage exists | ✓ | Witnessed (Ch 4) | Chapter 4
Password to vault | → | Told by mentor (Ch 6) | Chapter 6
Traitor is John | ? | Deduced from clues (Ch 8) | Chapter 8
```

**Rule**: Before character acts on information, CHECK THIS SHEET.

### POV-Specific Tracking

**For Multi-POV Stories**:

Each POV character has DIFFERENT knowledge at DIFFERENT times.

**Critical Checks**:
- Character A's POV can't reveal info only Character B knows (unless A learns it)
- When switching POVs, track what THAT character knows
- If character acts on information, trace how they got it

**Example Issue**:
> Chapter 5 (Alice POV): Alice finds the murder weapon in drawer.
> Chapter 7 (Bob POV): Bob searches the drawer, finds it empty.
>
> **PLOT HOLE**: What happened to weapon? Who moved it? When?

**Prevention**: Track object locations and who knows about them.

### The "How Did They Know?" Test

**Before any character action, ask**:
1. What information is this action based on?
2. How did character learn this information?
3. Is there a scene showing them learning it?
4. If not explicitly shown, can reader infer it reasonably?

**If answer to #4 is "no"**: PLOT HOLE. Fix by:
- Adding scene where they learn it
- Having them discover it on-page
- Showing investigation/deduction process
- Adjusting action to match their knowledge

## PART 2: TIMELINE CONSISTENCY

### The Problem

**Common Failures**:
- Character arrives before they could have left
- Event happens twice with different dates
- Season changes impossibly fast
- Character's age doesn't math
- Technology exists before it was invented in your world

### The Solution: Master Timeline

**Create comprehensive timeline**:

```
DAY | DATE | EVENTS | LOCATION | WHO'S PRESENT | NOTES
----|------|--------|----------|---------------|------
1 | Mon, Spring 3 | Hero leaves village | Village → Forest | Hero | Takes 3-day journey
2 | Tue, Spring 4 | Hero travels | Forest | Hero | Camps at river
3 | Wed, Spring 5 | Villain attacks city | City | Villain, Guards | Meanwhile...
4 | Thu, Spring 6 | Hero arrives city (sees smoke) | City outskirts | Hero | Arrives AFTER attack
```

**Key Principle**: Characters can only be in one place at one time. Travel takes time.

### Travel Time Calculator

**Prevent impossible arrivals**:

```
DISTANCE: _____ miles/km
TRAVEL METHOD: Walking / Horse / Car / Flight / Magic
TERRAIN: Easy / Moderate / Difficult
TRAVEL TIME: _____ days

DEPARTURE: Chapter ___, Day ___
ARRIVAL: Chapter ___, Day ___

CHECK: Does math work?
```

**Common Mistake**: Character leaves Ch 3 (Monday), arrives Ch 4 (Tuesday), but journey should take 5 days.

### Age Tracking

**For stories spanning years**:

```
CHARACTER: _______
BIRTH YEAR: _______

EVENT | YEAR | CHARACTER'S AGE
------|------|----------------
Story begins | 1450 | 16
Joins army | 1452 | 18
Battle of X | 1455 | 21
```

**Check**: Do character behaviors match their age?

### Seasonal/Weather Consistency

**Track seasons if they matter**:

```
CHAPTER | SEASON | WEATHER | IMPLICATIONS
--------|--------|---------|-------------
1-3 | Spring | Rainy | Muddy roads, slow travel
4-6 | Summer | Hot | Drought mentioned, rivers low
7 | FALL??? | SNOW??? | **ERROR**: Too early for snow
```

**Fix**: Either adjust season progression or change weather details.

## PART 3: MAGIC SYSTEM CONSISTENCY

### The Problem

Magic works differently in different scenes because you forgot the rules.

**Example Failures**:
- Ch 3: "Magic requires verbal spell"
- Ch 8: Character casts spell silently
- **CONTRADICTION**

### The Solution: Rule Tracking Sheet

**Document EVERY magic use**:

```
CHAPTER | WHO | SPELL/POWER | RULES USED | COST PAID | RESULT
--------|-----|-------------|------------|-----------|--------
3 | Hero | Fireball | Verbal + gesture + mana | 20 mana, exhaustion | Success
5 | Hero | Shield | Gesture only | 10 mana | **CONTRADICTION**: Didn't speak
```

**Before writing magic scene**:
1. Review rules you've established
2. Check previous uses of this power
3. Ensure NEW use matches previous pattern
4. If breaking pattern, EXPLAIN why (new skill, different situation, etc.)

### Magic Rule Change Log

**If you MUST change a rule mid-story**:

```
ORIGINAL RULE: Healing requires touch
CHANGED TO: Healing works at distance
CHAPTER OF CHANGE: Chapter 12
IN-STORY EXPLANATION: Character discovers advanced technique
RETROACTIVE CHECK: Do earlier scenes still make sense?
```

**Revision Task**: Go back and check if change creates contradictions.

## PART 4: WORLDBUILDING CONSISTENCY

### The Problem

Details about your world contradict each other.

**Example Failures**:
- Ch 2: "Magic is illegal"
- Ch 9: Characters openly use magic in town square with no consequence
- Ch 4: "City has 50,000 people"
- Ch 11: "The city's 500,000 citizens gathered..."

### The Solution: World Bible

**Create reference document**:

#### Geography

```
LOCATION: Capital City
POPULATION: 50,000
GOVERNMENT: Council of Five
CLIMATE: Temperate, rainy winters
MAJOR EXPORTS: Wool, iron
DISTANCE FROM:
- Port City: 3 days by horse
- Northern Border: 10 days
```

**Before mentioning location, CHECK YOUR BIBLE**.

#### Cultural Rules

```
CULTURAL ELEMENT: Magic Use
LEGAL STATUS: Illegal (punishable by exile)
EXCEPTIONS: Royal mages (licensed)
ENFORCEMENT: Magic Wardens patrol cities
SOCIAL ATTITUDE: Fear and distrust
```

**If character violates rule, there must be consequence OR explanation**.

#### Technology Level

```
TECH CATEGORY | AVAILABLE? | NOTES
--------------|------------|-------
Printing Press | YES | Invented 50 years ago
Gunpowder | NO | Doesn't exist in this world
Steam Power | NO | Magic prevents development
Eyeglasses | YES | Common among scholars
```

**Prevent**: Character using technology you haven't established exists.

### Consistency Audit Questions

**Before publishing, check**:
- [  ] Does magic always follow same rules?
- [  ] Are character ages consistent throughout?
- [  ] Do travel times math correctly?
- [  ] Is geography internally consistent (distances, terrain)?
- [  ] Does technology level stay constant (or progress logically)?
- [  ] Are cultural rules enforced consistently?
- [  ] Do currency values stay stable?
- [  ] Are government structures consistent?

## PART 5: CHARACTER BEHAVIOR CONSISTENCY

### The Problem

Character acts out of character with no explanation.

**Example Failures**:
- Established coward suddenly brave with no character growth shown
- Character who hates violence kills without hesitation
- Vegetarian character eats meat
- Character forgets their own expertise

### The Solution: Character Behavior Baseline

**For each character, establish**:

```
CHARACTER: _______

CORE TRAITS:
- _______________ (would NEVER do)
- _______________ (would ALWAYS do)
- _______________ (growth area - can change)

BASELINE BEHAVIOR:
- In combat: _______________
- When threatened: _______________
- With authority: _______________
- Under stress: _______________
- When lying: _______________
```

**If character acts against baseline**:
1. Have they grown enough to justify change?
2. Are circumstances EXTREME enough to force change?
3. Is there a scene showing internal conflict about change?

**If NO to all three**: OUT OF CHARACTER. Revise.

### Character Voice Consistency

**Track distinctive speech patterns**:

```
CHARACTER: _______
VOCABULARY: Formal / Casual / Technical / Regional
SENTENCE LENGTH: Short / Medium / Long / Varied
VERBAL TIC: _______________
NEVER SAYS: _______________
ALWAYS SAYS WHEN: _______________
```

**In revision, read all one character's dialogue in sequence** - does it sound like same person?

## PART 6: PLOT LOGIC CONSISTENCY

### The Problem

Plot events don't follow logical consequences.

**Example Failures**:
- Character breaks law publicly, no arrest
- Building burns down, never mentioned again
- Character dies, other characters don't react
- Valuable object lost, no one searches for it

### The Solution: Consequence Tracking

**Every significant event should have consequences**:

```
EVENT: Hero kills villain's brother (Ch 6)

IMMEDIATE CONSEQUENCES:
- Body discovered (Ch 6)
- Villain enraged (Ch 7)

MEDIUM-TERM CONSEQUENCES:
- Villain seeks revenge (Ch 8-10)
- Other characters learn of it (Ch 9)

LONG-TERM CONSEQUENCES:
- Hero haunted by kill (Ch 12)
- Affects final confrontation (Ch 15)
```

**If event has NO consequences**: Either cut it or add consequences.

### The "So What?" Test

After every major scene, ask:
1. **What changed?** (If nothing, cut the scene)
2. **Who knows about this?** (Track information spread)
3. **What happens next because of this?** (Cause and effect)
4. **Who's affected?** (More than just protagonist)

**Plot Hole Warning**: If major event happens and nobody reacts or it's never mentioned again.

## PART 7: REVISION CHECKLIST

### Pre-Publication Consistency Audit

**Timeline Pass**:
- [  ] Master timeline created and checked
- [  ] All travel times mathematically work
- [  ] Character ages consistent throughout
- [  ] Seasonal progression logical
- [  ] No character in two places at once

**Knowledge Pass**:
- [  ] Character knowledge matrix filled out
- [  ] No character acts on information they don't have
- [  ] POV characters only know what they should
- [  ] Information spread tracked accurately
- [  ] Deductions are reasonable given evidence

**Magic/Rules Pass**:
- [  ] Magic used consistently per established rules
- [  ] Costs paid every time
- [  ] Limitations respected
- [  ] No deus ex machina uses
- [  ] Changes explained in-story

**World Pass**:
- [  ] Geography never contradicts
- [  ] Population numbers stay consistent
- [  ] Cultural rules enforced (or violations have consequences)
- [  ] Technology level consistent
- [  ] Government/economy doesn't randomly change

**Character Pass**:
- [  ] Behavior matches established baseline (or growth is shown)
- [  ] Voice consistent for each character
- [  ] Character expertise used appropriately
- [  ] Character quirks maintained
- [  ] Out-of-character moments justified

**Logic Pass**:
- [  ] Major events have consequences
- [  ] Characters react realistically to events
- [  ] No convenient forgetting of important info
- [  ] Mysteries have discoverable clues
- [  ] Villain plots make sense from their POV

## TOOLS & TEMPLATES

### Spreadsheet Structure

**Create consistency tracking spreadsheet**:

**Sheet 1: Master Timeline**
- Columns: Day, Date, Event, Location, Characters Present, Notes

**Sheet 2: Character Knowledge**
- Columns: Information, Character 1 (Y/N), Character 2 (Y/N), How Learned, When Learned

**Sheet 3: Magic Uses**
- Columns: Chapter, Caster, Spell, Rules Used, Cost Paid, Success/Fail, Notes

**Sheet 4: World Bible**
- Sections: Geography, Culture, Technology, History, Economy, Government

**Sheet 5: Character Baselines**
- Rows per character: Traits, Speech Pattern, Behavior Baseline, Growth Arc

### Simple Tracking for Pantsers

**Don't want huge spreadsheets? Minimum tracking**:

**1. Scene Cards**
- Who's present
- What they learn
- When it happens

**2. Character Knowledge Notes**
- After each scene, update simple list of "Character A now knows: X, Y, Z"

**3. World Notes**
- Document facts as you create them
- Before contradicting, search your notes

**4. "Awk ward" Tracker**
- Flag moments that feel inconsistent as you write
- Come back in revision to check/fix

## COMMON PLOT HOLES & FIXES

### Plot Hole: Impossible Knowledge

**Example**: Character knows password without being told.

**Fixes**:
- Add scene where they learn it
- Show them finding written note
- Another character tells them on-page
- They deduce it from evidence (show deduction)

### Plot Hole: Contradictory Magic

**Example**: Magic that required components suddenly doesn't.

**Fixes**:
- Ensure all uses include components
- Explain why this time is different (emergency technique, skill growth)
- Retcon earlier scene to match new version
- Add cost for breaking the rule

### Plot Hole: Timeline Impossible

**Example**: Character arrives before they should.

**Fixes**:
- Adjust timeline to add travel time
- Use faster travel method
- Change scene order
- Add "three days later" transition

### Plot Hole: Forgotten Consequences

**Example**: Major battle happens, never affects later events.

**Fixes**:
- Reference event in later chapters
- Show long-term impacts (PTSD, political change, etc.)
- Have other characters mention it
- Make it affect final climax

### Plot Hole: Out-of-Character Behavior

**Example**: Pacifist suddenly kills.

**Fixes**:
- Show extreme circumstances forcing change
- Internal monologue showing conflict
- Other characters notice change
- Make it part of character arc (moral descent or growth)

## INTEGRATION WITH SANDERSON SKILLS

### How This Works With Other Skills

**Promise-Progress-Payoff**:
- Promises require consistency (payoff must match setup)
- Track what was promised to ensure payoff delivers

**Proactive-Relatable-Capable**:
- Character behavior must match established pillars
- Knowledge limits affect what actions they can take

**Sanderson's Laws of Magic**:
- This guide helps enforce Law 1 (understanding) through consistency
- Tracks Law 2 (limitations) compliance

**Worldbuilding Tools**:
- This guide is the implementation of "coherence over density"
- Tracks the iceberg (what you know vs. what's shown)

## FINAL WISDOM

**Prevention > Cure**: Track as you write, not only in revision.

**When in Doubt, Check**: Better to spend 30 seconds checking your notes than create plot hole.

**Readers Notice**: Inconsistencies break immersion. They WILL catch errors you miss.

**It's Okay to Fix**: Finding plot hole in revision isn't failure—it's opportunity to improve.

---

*This guide ensures your carefully crafted story doesn't undermine itself with preventable plot holes and inconsistencies.*
