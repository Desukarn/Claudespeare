# Name Generator Requirement - Anti-AI-Slop System

## CRITICAL RULE: NO AI-GENERATED NAMES

**This is a BLOCKING requirement**: Claude MUST NOT generate character names directly. All names must come from external name generators.

## Why This Exists

AI models (including Claude) have strong biases toward certain names that appear constantly in AI-generated fiction:

**Common AI Slop Names (NEVER USE)**:
- Kael, Kaelin, Kylar, Kain
- Elara, Elora, Elysia, Elira
- Lyra, Lira, Liora
- Aria, Arya, Ariana
- Theron, Theron, Talon
- Zara, Zira, Zyra
- Aiden, Aric, Alistair
- Seraphina, Celestia
- Raven, Rook, Wren (as first names)
- Ash, Asher (overused)
- Any name ending in -ael, -ara, -lyn, -el, -a

These names are statistical artifacts of training data, NOT creative choices.

---

## THE RULE: Use Online Name Generators

When character names are needed, Claude MUST:

1. **Use WebFetch to access real name generators**
2. **Never generate names directly**
3. **Provide multiple options from generator**
4. **Let user choose or regenerate**

---

## Approved Name Generator Sources

### For Fantasy Names:
- **Fantasy Name Generators**: https://www.fantasynamegenerators.com/
  - Multiple cultural/racial options
  - Contextual (thieves, nobles, warriors, etc.)
  - Genre-specific (high fantasy, dark fantasy, etc.)

- **Behind the Name**: https://www.behindthename.com/random/
  - Historical names with meanings
  - Cultural authenticity
  - Can filter by region/era

- **Seventh Sanctum**: https://www.seventhsanctum.com/index-name.php
  - Various name generators
  - Good for unusual settings

### For Modern/Contemporary Names:
- **Behind the Name (Modern)**: https://www.behindthename.com/random/
- **Baby Name Wizard**: https://www.babynamewizard.com/
- **SSA Baby Names**: https://www.ssa.gov/OACT/babynames/ (for US period accuracy)

### For Sci-Fi Names:
- **Sci-Fi Name Generators**: https://www.fantasynamegenerators.com/sci-fi-names.php
- **Behind the Name (Futuristic)**: https://www.behindthename.com/random/

### For Historical Fiction:
- **Behind the Name (Historical)**: https://www.behindthename.com/random/
  - Can filter by time period and region
- **Medieval Names**: https://www.behindthename.com/random/ (filter: Medieval)

---

## Workflow: How to Get Names

### Step 1: Determine Context
- Genre (fantasy, sci-fi, contemporary, historical)
- Culture/ethnicity (if specified)
- Character role (noble, commoner, villain, etc.)
- Time period (medieval, modern, futuristic)

### Step 2: Choose Appropriate Generator
Match generator to context:
- Fantasy thief → Fantasy Name Generators (rogue names)
- Victorian detective → Behind the Name (1800s British)
- Space pilot → Sci-Fi Name Generators
- Modern CEO → Behind the Name (contemporary)

### Step 3: Use WebFetch to Get Names
```
Use WebFetch tool with appropriate generator URL
Extract 5-10 name options
Present to user with context
```

### Step 4: User Selection
User can:
- Choose from options
- Ask for more options (different generator or regenerate)
- Provide their own name

---

## Implementation in Planning Skills

### In `indepth-plan.md` - Step 3: Character Development

**REPLACE THIS**:
```
#### Name
"What's this character's name?"

Provide genre-appropriate examples if needed.
```

**WITH THIS**:
```
#### Name
"I'll use an online name generator to provide authentic options. Hold on..."

**CRITICAL**: Do NOT generate names yourself. Use WebFetch with appropriate name generator.

**Workflow**:
1. Determine character context (genre, role, culture)
2. Choose appropriate generator from name-generator-requirement.md
3. Use WebFetch to fetch 5-10 name options
4. Present options to user:
   ```
   Here are 10 authentic {genre/culture} names from {generator source}:

   1. [Name] (meaning: [if available])
   2. [Name] (meaning: [if available])
   3. [Name]
   4. [Name]
   5. [Name]
   6. [Name]
   7. [Name]
   8. [Name]
   9. [Name]
   10. [Name]

   Pick a number (1-10), ask for more options, or provide your own name.
   ```

5. User selects or requests more
6. If user requests more, use different generator or regenerate

**NEVER**:
- Generate names like "Kael", "Elara", "Lyra", "Aria", etc.
- Use names from AI training data artifacts
- Skip the generator and provide "suggestions"
```

### In `yolo-expand.md` - Character Creation

**ADD SAME RULE**:
```
### Generating Character Names

**CRITICAL**: Use name-generator-requirement.md workflow.

For YOLO mode (faster), still use generator but:
- Fetch 5 names instead of 10
- User can quick-select or type "1" for first option
- If user says "just pick one", use first option from generator

**NEVER generate names directly** even in YOLO mode.
```

---

## Example: Correct Workflow

**User**: "Create a fantasy thief character"

**Claude**:
```
I'll get authentic fantasy thief names from Fantasy Name Generators. Hold on...

[Uses WebFetch: https://www.fantasynamegenerators.com/fantasy-names.php or similar]

Here are 10 fantasy rogue/thief names:

1. Garrett Thorn
2. Mira Shadowstep
3. Finn Quickblade
4. Silas Blackwood
5. Nora Whisper
6. Tobias Lockhart
7. Vesper Nightingale
8. Rowan Silvertongue
9. Cassian Grey
10. Thalia Ravenwood

Pick a number (1-10), ask for more options, or provide your own name.
```

**User**: "I'll take 2"

**Claude**: "Great! Your character is named Mira Shadowstep."

---

## Example: Incorrect Workflow (AI SLOP)

**User**: "Create a fantasy thief character"

**Claude** ❌:
```
How about "Kael Shadowborn"? Or "Elara Nightwhisper"?
```

**This is WRONG**:
- Kael is AI slop name #1
- Elara is AI slop name #2
- "Shadowborn", "Nightwhisper" are also overused AI patterns
- No generator used

---

## Enforcement

**In Planning Skills**:
- Add explicit "use WebFetch with generator" step
- List approved generators
- Show example workflow
- Add warning: "Never generate names directly"

**In Character Bank**:
- When updating characters, check if name is from AI slop list
- Warn user: "This name is commonly AI-generated. Consider using a name generator for authenticity."

**In Revision**:
- Add name check to `/write:detect` (AI pattern detection)
- Flag common AI slop names
- Suggest using generator for replacements

---

## AI Slop Name Detection (For Revision)

Add to `/write:detect` or `/write:revise`:

```python
AI_SLOP_NAMES = [
    "kael", "kaelin", "kylar", "kain",
    "elara", "elora", "elysia", "elira",
    "lyra", "lira", "liora",
    "aria", "arya", "ariana",
    "theron", "talon",
    "zara", "zira", "zyra",
    "aiden", "aric", "alistair",
    "seraphina", "celestia",
    "raven", "rook", "wren"  # as first names only
]

def check_names(character_names):
    flagged = []
    for name in character_names:
        if name.lower() in AI_SLOP_NAMES:
            flagged.append(name)

    if flagged:
        return f"⚠️ AI-generated name patterns detected: {', '.join(flagged)}\n" \
               f"These names are statistical artifacts common in AI writing.\n" \
               f"Consider using /write:name-generator to replace with authentic names."
    return None
```

---

## Benefits of This System

1. **Authenticity**: Real names from cultural/historical sources
2. **Diversity**: Access to thousands of names from many cultures
3. **Meaning**: Many generators provide name meanings
4. **Anti-Slop**: Eliminates AI training data artifacts
5. **User Choice**: Multiple options, not single AI suggestion
6. **Professional Quality**: Names feel researched, not generated

---

## Quick Reference

**When naming characters**:
1. ❌ DON'T: Generate names yourself
2. ✅ DO: Use WebFetch with name generator
3. ✅ DO: Provide 5-10 options
4. ✅ DO: Let user choose or regenerate
5. ❌ DON'T: Use Kael, Elara, Lyra, Aria, or other AI slop names

**Approved Generators**:
- Fantasy Name Generators (fantasy/sci-fi)
- Behind the Name (historical/modern/any)
- Seventh Sanctum (unusual settings)

---

*This system is MANDATORY for all Claudespeare character creation workflows.*
