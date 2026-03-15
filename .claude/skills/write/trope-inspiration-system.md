# Trope Inspiration System - Anti-Cookie-Cutter Story Generator

## PROBLEM: Claude Generates Formulaic Plots

**Common AI Story Patterns (AVOID)**:
- "Strength becomes weakness" arcs
- "Final moral act" redemptions
- "Greed corrupts protagonist" tragedies
- "Mentor dies to motivate hero"
- "Dark secret revealed at midpoint"
- "Power costs humanity" magic systems
- "Chosen one refuses call, accepts later"
- "Villain has tragic backstory"
- "Love interest dies for motivation"
- "Prophecy subverted at climax"

These are **not creative choices** - they're statistical patterns from training data.

---

## SOLUTION: TVTropes Research Agent

Before planning story, spawn research agent to:
1. Browse TVTropes for random trope combinations
2. Find unexpected/interesting tropes that fit genre
3. Avoid overused patterns
4. Create unique trope combinations

---

## Workflow: Story Initialization with Trope Research

### Step 1: After User Provides Premise

User gives premise (e.g., "Thief steals fairy in bottle, tragedy")

**BEFORE planning**, launch research agent:

```
TASK: Find unexpected tropes for story inspiration

PREMISE: [user's premise]
GENRE: [user's genre]

INSTRUCTIONS:
1. Use WebFetch to browse TVTropes.org
2. Find 3-4 random tropes from these categories:
   - Plot tropes (NOT the obvious ones for this genre)
   - Character tropes (avoid Hero's Journey clichés)
   - Setting tropes
   - Unexpected twists for this genre
3. Avoid common AI patterns:
   - "Strength becomes weakness"
   - "Final moral act"
   - "Mentor dies"
   - "Power corrupts"
   - Standard chosen one narratives
4. Look for COMBINATIONS that create unique angles
5. Return 8-10 trope options with explanations

GOAL: Make this story feel fresh, not like every other AI-generated story
```

---

## TVTropes Categories to Browse

### For Plot Inspiration:
- **Unexpected Plot Twists**: https://tvtropes.org/pmwiki/pmwiki.php/Main/PlotTwist
- **Subverted Tropes**: https://tvtropes.org/pmwiki/pmwiki.php/Main/SubvertedTrope
- **Unconventional Story Structure**: https://tvtropes.org/pmwiki/pmwiki.php/Main/NarrativeDevices

### For Character Inspiration:
- **Character Archetypes** (find unusual ones): https://tvtropes.org/pmwiki/pmwiki.php/Main/CharacterizationTropes
- **Anti-Hero Variations**: https://tvtropes.org/pmwiki/pmwiki.php/Main/AntiHero
- **Unconventional Protagonists**: https://tvtropes.org/pmwiki/pmwiki.php/Main/UnconventionalCharacter

### For Avoiding Clichés:
- **Overused Tropes**: https://tvtropes.org/pmwiki/pmwiki.php/Main/OverusedPlotDevice
- **Dead Horse Tropes**: https://tvtropes.org/pmwiki/pmwiki.php/Main/DeadHorseTrope

### For Unique Twists:
- **Genre Deconstruction**: https://tvtropes.org/pmwiki/pmwiki.php/Main/Deconstruction
- **Zig-Zagged Tropes**: https://tvtropes.org/pmwiki/pmwiki.php/Main/ZigZaggingTrope

---

## Example: Thief + Fairy Story

**INSTEAD OF** (AI slop):
- Greed corrupts thief
- Strength (proactivity) becomes weakness
- Final moral act = self-destruction
- Tragedy = gets what he wants, loses what he needs

**TVTropes Research Might Find**:
1. **Villainous Rescue** - Fairy saves thief at critical moment (unexpected ally)
2. **Earn Your Bad Ending** - Thief succeeds but outcome is hollow (not corruption, just emptiness)
3. **Blue-and-Orange Morality** - Fairy operates on non-human ethics thief can't understand
4. **Spanner in the Works** - Sister's illness was actually protecting her from something
5. **Karmic Jackpot** - Thief's greed accidentally solves bigger problem
6. **Wrong Genre Savvy** - Thief thinks he's in heist story, actually in cosmic horror
7. **Fridge Horror** - Ending seems okay until you realize implications
8. **Pyrrhic Villainy** - Fairy escapes but at cost that makes freedom meaningless
9. **No Sympathy** - Story doesn't try to make you pity thief (bold choice)
10. **Bittersweet Ending** - Not pure tragedy, something good comes from disaster

**Result**: Mix and match these to create UNIQUE story, not formulaic tragedy #7294

---

## Implementation in Planning Workflow

### In `new-project.md` - After Step 8 (Themes)

**ADD NEW STEP**:

```markdown
### Step 9: Trope Inspiration (Optional but Recommended)

**Question:** "Would you like me to research story tropes for fresh inspiration?"

**Options:**
A. Yes - Launch TVTropes research agent (recommended, takes 2-3 minutes)
B. No - Proceed with planning directly

**If YES**:

I'll spawn a research agent to browse TVTropes and find unexpected trope combinations for your story.

[Launch Task agent with prompt from trope-inspiration-system.md]

Agent returns 8-10 trope suggestions. Present to user:

```
Based on TVTropes research, here are fresh angle ideas for your story:

PLOT TROPES:
1. [Trope Name] - [Explanation of how it applies]
2. [Trope Name] - [Explanation]

CHARACTER TROPES:
3. [Trope Name] - [Explanation]
4. [Trope Name] - [Explanation]

TWIST TROPES:
5. [Trope Name] - [Explanation]
6. [Trope Name] - [Explanation]

STRUCTURAL TROPES:
7. [Trope Name] - [Explanation]
8. [Trope Name] - [Explanation]

Pick 2-3 tropes to weave into your story, or ask for more options.
```

**User selects 2-3 tropes**

**Store**: `INSPIRATION_TROPES` (array)

**Use during planning**: Reference these tropes when building plot/characters to avoid cookie-cutter patterns
```

---

## Integration with Sanderson Skills

**Promise-Progress-Payoff** + **Tropes**:
- Sanderson framework provides STRUCTURE
- Tropes provide UNIQUE CONTENT
- Result: Structured but not formulaic

**Example**:
- Framework: "Major Dramatic Question by Act 1 end"
- Trope: "Wrong Genre Savvy" (protagonist thinks it's different story type)
- Result: Question is established, but NOT the obvious one

---

## Research Agent Prompt Template

```
You are a trope research specialist. Your job is to find UNEXPECTED, INTERESTING trope combinations from TVTropes that will make a story feel fresh.

PREMISE: {user_premise}
GENRE: {user_genre}
THEMES: {user_themes}

TASK:
1. Browse TVTropes using WebFetch
2. Find 8-10 tropes across these categories:
   - 2-3 Plot structure tropes (avoid obvious genre conventions)
   - 2-3 Character tropes (avoid Hero's Journey clichés)
   - 2-3 Twist/subversion tropes
   - 1-2 Meta/structural tropes

CRITICAL REQUIREMENTS:
- AVOID these overused AI patterns:
  * "Strength becomes weakness"
  * "Final moral act"
  * "Power corrupts protagonist"
  * "Mentor dies"
  * Standard chosen one narratives
  * "Gets what they want, loses what they need"

- LOOK FOR:
  * Unexpected genre combinations
  * Subverted expectations
  * Unusual character dynamics
  * Fresh takes on familiar premises
  * Tropes that COMBINE in interesting ways

FORMATTING:
For each trope:
**[Trope Name]** ([Link to TVTropes page])
- **What it is**: [Brief explanation]
- **How it applies**: [Specific application to this story]
- **Why it's fresh**: [Why this avoids cliché]

GOAL: Give the writer 8-10 building blocks that will make their story feel unique, not like every other AI-generated story in this genre.
```

---

## Example Output: Thief + Fairy Tragedy

**Research Agent Returns**:

### PLOT TROPES:

**1. Earn Your Bad Ending** (https://tvtropes.org/pmwiki/pmwiki.php/Main/EarnYourBadEnding)
- **What it is**: Protagonist makes deliberately bad choices and earns disaster
- **How it applies**: Thief isn't corrupted by magic - he CHOOSES greed consciously each time
- **Why it's fresh**: Not "power corrupts" (passive), but "I chose this" (active agency)

**2. Fridge Horror** (https://tvtropes.org/pmwiki/pmwiki.php/Main/FridgeHorror)
- **What it is**: Ending seems okay until you think about implications
- **How it applies**: Sister is "saved" but now what? What did thief unleash?
- **Why it's fresh**: Not immediate tragedy, delayed realization

**3. Shaggy Dog Story** (https://tvtropes.org/pmwiki/pmwiki.php/Main/ShaggyDogStory)
- **What it is**: Quest was pointless, MacGuffin didn't matter
- **How it applies**: Sister was never really sick? Fairy manipulated perception?
- **Why it's fresh**: Undermines entire premise in interesting way

### CHARACTER TROPES:

**4. Blue-and-Orange Morality** (https://tvtropes.org/pmwiki/pmwiki.php/Main/BlueAndOrangeMorality)
- **What it is**: Character operates on incomprehensible ethics
- **How it applies**: Fairy isn't evil OR good - operates on rules thief can't understand
- **Why it's fresh**: Not "villain with tragic backstory", genuinely alien

**5. Spanner in the Works** (https://tvtropes.org/pmwiki/pmwiki.php/Main/SpannerInTheWorks)
- **What it is**: Unpredictable element ruins everyone's plans
- **How it applies**: Sister's illness was PROTECTING her from fairy magic
- **Why it's fresh**: Inversion of "save the sick girl" trope

**6. Protagonist Journey to Villain** (https://tvtropes.org/pmwiki/pmwiki.php/Main/ProtagonistJourneyToVillain)
- **What it is**: Story ends with protagonist as new antagonist
- **How it applies**: Thief becomes new threat, fairy is free but now thief is imprisoned
- **Why it's fresh**: Role reversal, cyclical trap

### TWIST TROPES:

**7. The Dog Was the Mastermind** (https://tvtropes.org/pmwiki/pmwiki.php/Main/TheDogWasTheMastermind)
- **What it is**: Least suspected character orchestrated everything
- **How it applies**: SISTER planned this all along (not victim, manipulator)
- **Why it's fresh**: Completely inverts expected dynamics

**8. No Sympathy** (https://tvtropes.org/pmwiki/pmwiki.php/Main/NoSympathy)
- **What it is**: Story doesn't try to make you sympathize with protagonist
- **How it applies**: Thief is just greedy, no sad backstory, story judges him
- **Why it's fresh**: Bold to NOT make protagonist sympathetic in tragedy

### STRUCTURAL TROPES:

**9. Wrong Genre Savvy** (https://tvtropes.org/pmwiki/pmwiki.php/Main/WrongGenreSavvy)
- **What it is**: Character thinks they're in different story type
- **How it applies**: Thief thinks it's heist story, actually cosmic horror
- **Why it's fresh**: Genre shift mid-story

**10. Bittersweet Ending** (https://tvtropes.org/pmwiki/pmwiki.php/Main/BittersweetEnding)
- **What it is**: Not pure tragedy, something good emerges
- **How it applies**: Thief fails BUT fairy's escape fixes something else
- **Why it's fresh**: Avoids "everything is terrible" ending

---

**User selects**: 1, 4, 5, 9 (Earn Your Bad Ending, Blue-and-Orange Morality, Spanner in the Works, Wrong Genre Savvy)

**Story becomes**: Thief thinks he's in heist story (Genre Savvy), makes active greedy choices (Earn Bad Ending), fairy operates on incomprehensible ethics (Blue-Orange Morality), sister's illness was actually protective curse (Spanner).

**Result**: MUCH more interesting than "greed corrupts, strength becomes weakness, final moral act"

---

## Anti-Cliché Checklist

Before finalizing plot, check:

- [ ] Does protagonist's flaw follow "strength becomes weakness" pattern? (CLICHÉ)
- [ ] Does climax involve "final moral act" redemption? (CLICHÉ)
- [ ] Does magic system do "power corrupts" literally? (CLICHÉ)
- [ ] Does mentor die to motivate hero? (CLICHÉ)
- [ ] Does tragedy follow "gets want, loses need" exactly? (CLICHÉ)
- [ ] Is villain just "hero with tragic backstory"? (CLICHÉ)
- [ ] Does prophecy get subverted in obvious way? (CLICHÉ)

**If you checked ANY of these**: Go back to trope research, find fresh angle

---

## Adding to Revision Tools

### In `/write:detect` - Add Cliché Detection

```python
PLOT_CLICHES = [
    "strength becomes weakness",
    "final moral act",
    "power corrupts",
    "mentor dies",
    "chosen one refuses call",
    "gets what they want, loses what they need",
    "tragic backstory villain",
    "prophecy subverted"
]

def detect_plot_cliches(outline_text):
    found = []
    outline_lower = outline_text.lower()

    for cliche in PLOT_CLICHES:
        if cliche in outline_lower:
            found.append(cliche)

    if found:
        return f"⚠️ Common plot clichés detected: {', '.join(found)}\n" \
               f"Consider using /write:trope-research to find fresh angles."
    return None
```

---

## Benefits of This System

1. **Breaks AI Patterns**: Forces research beyond training data
2. **Unique Combinations**: Tropes mix in unexpected ways
3. **User Choice**: Writer picks what resonates
4. **Educational**: Writers learn about storytelling techniques
5. **Prevents Slop**: Both name slop AND plot slop caught

---

## Quick Reference

**When starting story**:
1. ❌ DON'T: Let Claude generate plot from scratch
2. ✅ DO: Research 8-10 tropes first
3. ✅ DO: Pick 2-3 unexpected combinations
4. ✅ DO: Build plot around those tropes
5. ❌ DON'T: Use "strength becomes weakness" or other AI clichés

**Approved Research Source**:
- TVTropes.org (comprehensive, well-organized)

---

*This system is MANDATORY for new story projects to prevent cookie-cutter plots.*
