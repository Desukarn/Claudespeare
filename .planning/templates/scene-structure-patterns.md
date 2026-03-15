# Scene Structure Pattern Database

This database defines formulaic scene structures commonly found in AI-generated fiction. These patterns create cookie-cutter, robotic pacing that signals algorithmic writing.

## Overview

AI-generated fiction often falls into predictable structural patterns:
- Opening scenes with weather/waking up repeatedly
- Mirror description clichés for character introduction
- Mechanical cliffhanger placement (every scene ends dramatically)
- Rigid action-reaction-introspection loops
- Formulaic scene arc structure with no variation

Detection scans for these patterns across all chapters to identify robotic scene construction.

---

## Pattern 1: Weather Opening Overuse

**Category:** Scene opening formula
**Why problematic:** Starting scenes with weather is fine occasionally, but AI overuses it as a default opening strategy

**Detection logic:**
1. Scan first 1-3 sentences of each scene (marked by scene breaks `---` or chapter starts)
2. Check for weather-related keywords:
   - Rain/raining/drizzle/storm/thunderstorm
   - Snow/snowing/blizzard/flurries
   - Sun/sunny/sunshine/bright
   - Wind/windy/breeze/gust
   - Fog/foggy/mist/misty
   - Cloud/cloudy/overcast
   - Weather descriptions: "the sky was", "the air was"
3. Count weather openings across all scenes
4. Calculate percentage: (weather openings / total scenes) × 100

**Thresholds:**
- 0-20%: Normal variety (acceptable)
- 21-35%: Noticeable pattern (warning)
- 36-50%: Formulaic (flag as issue)
- 51%+: Robotic (critical issue)

**Report format:**
```
Issue: Weather opening overuse
Pattern: {percentage}% of scenes open with weather description
Threshold: 35% maximum recommended
Severity: {Warning/Critical}
Examples:
  - Chapter 2, Scene 1: "Rain drummed against the windows"
  - Chapter 4, Scene 2: "The morning sun broke through clouds"
  - Chapter 7, Scene 1: "Fog rolled through the streets"
Suggestion: Vary scene openings. Try:
  - Dialogue
  - Action mid-scene (in media res)
  - Character's internal thought
  - Sensory detail (non-weather: sounds, smells)
  - Environmental detail specific to location
```

---

## Pattern 2: Wake-Up Scene Overuse

**Category:** Scene opening formula
**Why problematic:** Characters waking up is the easiest scene start, but using it repeatedly shows lazy structure

**Detection logic:**
1. Scan first paragraph of each scene
2. Check for wake-up keywords/phrases:
   - "woke" / "woke up" / "awoke" / "awakened"
   - "opened her eyes" / "opened his eyes"
   - "consciousness returned" / "came to"
   - "alarm" / "alarm clock"
   - "morning light" / "dawn"
   - "stretched" / "yawned" (within first 2 sentences)
   - References to dreams: "the dream faded", "nightmare", "still half-asleep"
3. Count wake-up openings across all chapters
4. Calculate percentage: (wake-up scenes / total chapters) × 100

**Thresholds:**
- 0-15%: Normal (acceptable - maybe 1-2 wake-ups in 10 chapters)
- 16-30%: Pattern emerging (warning)
- 31-50%: Formulaic (critical)
- 51%+: Robotic (severe)

**Special case:**
If story deliberately tracks daily routine (prison novel, medical drama with shifts), adjust threshold upward to 25% warning / 40% critical.

**Report format:**
```
Issue: Wake-up scene overuse
Pattern: {count} of {total} chapters begin with character waking up ({percentage}%)
Threshold: 15% maximum recommended (1-2 in typical novel)
Severity: {Warning/Critical}
Examples:
  - Chapter 1: "Sarah woke to the sound of rain"
  - Chapter 3: "The alarm dragged Marcus from sleep"
  - Chapter 6: "She opened her eyes to morning light"
Suggestion: Most chapter transitions can skip the waking moment. Start scenes:
  - Mid-action (character already engaged in activity)
  - At the inciting incident of the scene
  - With dialogue
  - At a decision point or conflict moment
Reserve wake-up scenes for:
  - Significant dream/nightmare with plot relevance
  - Morning after major event (shows character processing)
  - Jarring wake-up that starts conflict
```

---

## Pattern 3: Mirror Description Cliché

**Category:** Character introduction formula
**Why problematic:** Having characters look in mirrors to describe themselves is a well-known amateur/AI writing trope

**Detection logic:**
1. Scan for mirror-related keywords:
   - "mirror" / "reflection" / "reflected"
   - "looked at himself" / "looked at herself"
   - "saw his reflection" / "saw her reflection"
   - "bathroom mirror" / "reflective surface"
   - "glanced at her appearance" / "checked his appearance"
2. When found, check surrounding context (±3 sentences):
   - Does it include physical self-description?
   - Eye color mentioned?
   - Hair description?
   - General appearance cataloging?
3. Flag if mirror is used primarily for character description dump
4. Count instances across story

**Thresholds:**
- 0-1 instances: Acceptable (maybe one character is vain or checking injury)
- 2 instances: Warning (pattern emerging)
- 3+ instances: Critical (formulaic character introduction)

**Report format:**
```
Issue: Mirror description cliché
Pattern: {count} instance(s) of character self-description via mirror
Threshold: 1 maximum (preferably 0)
Severity: {Warning/Critical}
Examples:
  - Chapter 1: "Sarah looked in the bathroom mirror. Her green eyes were tired, her black hair messy."
  - Chapter 5: "Marcus checked his reflection. The scar on his jaw was healing."
Suggestion: Readers don't need complete physical descriptions. Integrate appearance details naturally:
  - Other characters' observations in dialogue/thought
  - Action-based description ("She brushed her long hair back")
  - Contrast with another character ("taller than Marcus")
  - Detail revealed through interaction ("Her green eyes narrowed")
  - Skip appearance details that don't matter to the story
Use mirrors only for:
  - Character noticing a change (injury, aging, transformation)
  - Vanity as character trait
  - Plot-relevant checking (disguise, makeover)
```

---

## Pattern 4: Cliffhanger Every Scene

**Category:** Mechanical tension structure
**Why problematic:** Ending every scene/chapter with dramatic tension becomes predictable and exhausting

**Detection logic:**
1. Extract final 1-2 sentences of each scene/chapter
2. Check for cliffhanger markers:
   - Questions: sentence ends with "?"
   - Shock/revelation: "couldn't be", "impossible", "no way", "what if"
   - Sudden appearance: "turned around and saw", "door burst open", "voice behind"
   - Ominous foreshadowing: "little did she know", "would soon regret", "everything changed"
   - Single-word dramatic fragments: "And then—", "Unless..."
   - Ellipses: ends with "..."
3. Count scenes ending with cliffhanger markers
4. Calculate percentage: (cliffhanger endings / total scenes) × 100

**Thresholds:**
- 0-40%: Good variety (acceptable)
- 41-60%: Predictable pattern (warning)
- 61-80%: Formulaic (critical)
- 81-100%: Robotic (severe - every scene ends dramatically)

**Report format:**
```
Issue: Cliffhanger overuse (mechanical tension)
Pattern: {percentage}% of scenes end with dramatic tension markers
Threshold: 40% maximum recommended
Severity: {Warning/Critical/Severe}
Examples:
  - Chapter 1: "Then she saw the body."
  - Chapter 2: "The door burst open. Marcus stood there, covered in blood."
  - Chapter 3: "Unless... no. It couldn't be."
  - Chapter 5: "She turned around and gasped."
Analysis: {X} of {Y} scenes end with cliffhanger structure
Suggestion: Vary scene endings for natural rhythm:
  - Quiet resolutions (40%): Scene ends with decision, arrival, or rest
  - Mid-action transitions (20%): Cut during normal activity, pick up next scene
  - Emotional beats (20%): Character feeling/reflection
  - Dramatic cliffhangers (20%): Save for major reveals or act breaks
Benefits of variety:
  - Builds trust (reader knows not every moment is crisis)
  - Makes real cliffhangers more impactful
  - Creates breathing room and pacing variation
  - Feels human, not algorithmic
```

---

## Pattern 5: Action-Reaction-Introspection Loop

**Category:** Scene internal structure formula
**Why problematic:** Rigid A-R-I pattern in every scene creates mechanical, predictable prose

**Detection logic:**
1. For each scene, analyze paragraph-level structure:
   - Action paragraphs: dialogue, physical action, external events
   - Reaction paragraphs: character response (emotion, physical reaction)
   - Introspection paragraphs: internal thought, analysis, memory
2. Check for repeating pattern:
   - Action → Reaction → Introspection → Action → Reaction → Introspection
   - Specifically: 3+ consecutive A-R-I loops within single scene
3. Flag scenes that follow rigid loop structure
4. Count across story

**Detection markers:**
- **Action:** Dialogue tags, action verbs, external stimulus
- **Reaction:** "She felt", "His heart", "Her stomach", physical sensation
- **Introspection:** "She thought", "He wondered", "Why had", memory/analysis

**Thresholds:**
- 0-20% scenes: Normal (acceptable - occasional clear structure)
- 21-40% scenes: Pattern emerging (warning)
- 41-60% scenes: Formulaic (critical)
- 61%+ scenes: Robotic (severe)

**Report format:**
```
Issue: Rigid action-reaction-introspection loop structure
Pattern: {percentage}% of scenes follow mechanical A-R-I pattern
Threshold: 20% maximum
Severity: {Warning/Critical/Severe}
Examples:
  Chapter 4, Scene 2:
    Para 1: [Action] Marcus opened the door
    Para 2: [Reaction] Sarah's heart pounded
    Para 3: [Introspection] She wondered why he'd come
    Para 4: [Action] "What do you want?" she asked
    Para 5: [Reaction] Her hands trembled
    Para 6: [Introspection] This reminded her of before
Suggestion: Vary scene micro-structure:
  - Action without immediate reaction (let tension build)
  - Reaction without introspection (stay in moment)
  - Introspection during action (thoughts while moving)
  - Dialogue without internal commentary (trust subtext)
  - Multiple actions before reaction (rapid pacing)
  - Extended introspection without action (slow, contemplative)
Benefits:
  - Natural rhythm variation
  - Some moments feel immediate, others reflective
  - Reader doesn't predict paragraph pattern
  - More sophisticated prose architecture
```

---

## Pattern 6: Three-Act Scene Structure Overuse

**Category:** Scene arc formula
**Why problematic:** Every scene following setup-conflict-resolution creates sameness

**Detection logic:**
1. For scenes longer than 500 words, analyze structure:
   - First 1/3: Introduction, character enters, situation established
   - Middle 1/3: Conflict, problem, tension introduced
   - Final 1/3: Resolution, decision, character exits
2. Check for mechanical adherence:
   - Scene length very consistent (all scenes 800-1200 words)
   - Every scene has clear three-part structure
   - No scenes that break the mold (all setup, all conflict, fragmented)
3. Flag if 60%+ of scenes follow identical arc pattern

**Thresholds:**
- 0-50%: Healthy variety (acceptable)
- 51-70%: Pattern emerges (warning)
- 71-85%: Formulaic (critical)
- 86-100%: Robotic (severe - every scene identical)

**Report format:**
```
Issue: Three-act scene structure overuse
Pattern: {percentage}% of scenes follow identical setup-conflict-resolution arc
Threshold: 50% maximum
Severity: {Warning/Critical/Severe}
Suggestion: Vary scene structures:
  - In medias res scenes (start mid-conflict, no setup)
  - Sequel scenes (all reflection/processing, no new conflict)
  - Failed resolution (scene ends without solving problem)
  - Multi-part scenes (several small conflicts in sequence)
  - Incomplete scenes (cut before resolution for pacing)
  - Quiet scenes (character moment, no conflict)
Benefits:
  - Pacing variety (fast/slow rhythm)
  - Reader can't predict scene shape
  - Some scenes breathe, others sprint
  - Mirrors real experience (not every interaction is a mini-story)
```

---

## Pattern 7: Scene Length Uniformity

**Category:** Pacing formula
**Why problematic:** All scenes/chapters same length signals algorithmic construction

**Detection logic:**
1. Calculate word count for each scene and chapter
2. Compute average and standard deviation
3. Flag if standard deviation is very low (scenes are all similar length)

**Analysis:**
- Extract all scene/chapter word counts
- Calculate mean (average) word count
- Calculate standard deviation
- Check for uniformity:
  - SD < 15% of mean: Very uniform (critical)
  - SD < 25% of mean: Uniform pattern (warning)
  - SD > 25% of mean: Natural variety (good)

**Thresholds:**
- Standard deviation > 25% of mean: Healthy variety
- Standard deviation 15-25% of mean: Warning (too uniform)
- Standard deviation < 15% of mean: Critical (robotic uniformity)

**Example calculation:**
```
Chapters: 2000, 1950, 2050, 2000, 1980, 2020, 2000 words
Mean: 2000 words
Standard deviation: 32 words (1.6% of mean)
→ Critical: All chapters within 100 words of each other
```

**Report format:**
```
Issue: Robotic scene/chapter length uniformity
Pattern: All chapters {min}-{max} words (SD: {sd}, {percentage}% of mean)
Threshold: SD should be >25% of mean for natural variety
Severity: {Warning/Critical}
Analysis:
  Mean chapter length: {mean} words
  Standard deviation: {sd} words ({percentage}% of mean)
  Range: {min} to {max}
Examples:
  - Chapter 1: 2000 words
  - Chapter 2: 1950 words
  - Chapter 3: 2050 words
  [All within 100 words of each other]
Suggestion: Vary scene/chapter length naturally:
  - Short chapters for tension/pacing (500-1000 words)
  - Long chapters for complex scenes (3000-5000 words)
  - Mix lengths based on content, not formula
  - Action scenes can be brief, emotional scenes longer
  - Don't force every chapter to hit target word count
Benefits:
  - Natural pacing variation
  - Matches content needs (not arbitrary structure)
  - Reader feels organic storytelling
  - Short chapters after long create rhythm
```

---

## Pattern 8: Formulaic Scene Opening Variety

**Category:** Opening structure analysis
**Why problematic:** If scenes rotate through 3-4 opening types predictably, it signals formula

**Detection logic:**
1. Categorize each scene opening:
   - Dialogue opening: First sentence is dialogue
   - Action opening: Character performing physical action
   - Setting opening: Location/environment description
   - Weather opening: Weather as first detail
   - Introspection opening: Character's thoughts
   - Time marker opening: "Three days later", "The next morning"
2. Check for rotation pattern:
   - Does story cycle through types predictably?
   - Action → Dialogue → Setting → Action → Dialogue → Setting (pattern)
3. Analyze distribution:
   - One type dominates >50%: Overuse
   - Perfect rotation (mechanical alternation): Formulaic
   - Random-seeming variety: Natural

**Thresholds:**
- Single type >50%: Overuse of one opening style
- Mechanical rotation detected: Formulaic (cycling through 3-4 types in order)
- Even distribution with no pattern: Natural (goal)

**Report format:**
```
Issue: Formulaic scene opening rotation
Pattern: Mechanical alternation detected
Analysis:
  Scene 1: Dialogue opening
  Scene 2: Action opening
  Scene 3: Setting opening
  Scene 4: Dialogue opening (pattern repeats)
  Scene 5: Action opening
  Scene 6: Setting opening
  Pattern: 3-type rotation (Dialogue → Action → Setting, repeat)
Severity: Warning
Suggestion: Break the rotation:
  - Choose opening based on scene's needs, not formula
  - Two dialogue openings in a row is fine
  - Mix unpredictably
  - Some scenes can start multiple ways simultaneously (dialogue while acting)
Alternative issue - Single opening type dominance:
Pattern: {percentage}% of scenes open with {type}
Suggestion: Expand opening variety:
  - Current heavy use: {dominant_type} ({percentage}%)
  - Try more: {underused_types}
```

---

## Detection Workflow Integration

### When to Run

Run scene structure detection:
- After completing 5+ chapters (patterns emerge across multiple chapters)
- Before final revision
- When prose "feels formulaic" but you can't identify why
- As part of comprehensive quality audit

### How to Use Results

**For individual violations:**
- Review flagged scenes
- Vary opening types, endings, internal structure
- Revise specific scenes to break patterns

**For systemic patterns (>50% of scenes):**
- Indicates deep structural formula
- May need to rewrite multiple scenes
- Consider: Was story outlined with formula? Or AI-assisted with pattern reinforcement?

**Severity prioritization:**
1. Critical issues (>60% threshold violations): Fix first
2. Warning issues (40-60%): Address during revision
3. Note issues (<40%): Consider, but may be acceptable for genre/style

### Output Format

Scene structure analysis should generate dedicated section in CONSISTENCY-REPORT.md or separate SCENE-STRUCTURE-REPORT.md:

```markdown
---
story: {project-slug}
report_type: scene_structure_analysis
checked: {ISO timestamp}
chapters_scanned: {count}
scenes_scanned: {count}
patterns_detected: {count}
---

# Scene Structure Pattern Analysis

## Summary

Scanned {N} scenes across {M} chapters.

**Patterns detected:**
- Weather openings: {percentage}% ({severity})
- Wake-up scenes: {count} chapters ({severity})
- Mirror descriptions: {count} instances ({severity})
- Cliffhanger endings: {percentage}% ({severity})
- A-R-I loops: {percentage}% ({severity})
- Scene length uniformity: SD {percentage}% ({severity})

## Detailed Findings

[Each pattern section with examples and suggestions]

## Priority Actions

1. [Most critical pattern to fix]
2. [Second priority]
3. [Third priority]

## Next Steps

- Revise flagged scenes to break patterns
- Re-run detection after fixes
- Consider whether patterns are genre-appropriate
```

---

## Notes

**Genre considerations:**

- **Thriller/Mystery:** Cliffhanger tolerance higher (50-60% acceptable)
- **Romance:** Wake-up scenes slightly more acceptable (intimate morning-after moments)
- **Literary fiction:** Lower tolerance for all formula (aim for <30% on all metrics)
- **YA/MG:** Some pattern okay (younger readers appreciate structure)

**Intentional pattern vs. AI formula:**

Some patterns might be intentional:
- Weather in gothic horror (atmospheric)
- Daily routine tracking in slice-of-life
- Consistent scene length in experimental fiction

Flag patterns but allow writer judgment on whether to revise.

---

**Last Updated:** 2026-03-14

## Maintenance

This template provides detection logic for scene structure patterns. The revision workflow reads this file to scan chapters for formulaic construction.

Writers can adjust thresholds in their project-specific copy if genre requires different tolerances.
