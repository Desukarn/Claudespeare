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

## Part 2: Place Naming System

**CRITICAL RULE:** Apply same anti-AI-slop standards to place names.

### Common AI Slop Place Names (NEVER USE)

**Banned Patterns:**
- Shadow + [anything]: Shadowmere, Shadowkeep, Shadowfen
- Dark + [anything]: Darkwood, Darkhaven, Darkwater
- Storm + [anything]: Stormkeep, Stormreach, Stormhaven
- [Color] + [Generic]: Redwood, Blackwater, Greenmoor
- Dragon + [noun]: Dragonspire, Dragonkeep
- Generic fantasy: The Fallen Kingdom, The Lost City

These are AI training data artifacts, not creative place naming.

---

### Approved Place Naming Methods

**Method 1: Cultural Pattern Research**

Use WebFetch to research real-world naming patterns:

**Germanic Cities:**
```
Research German town suffixes and roots
Suffixes: -heim (home), -burg (fortress), -wald (forest)
Roots: Eisen (iron), Rot (red), Grün (green)
Generate: Eisenheim, Rotenburg, Grünwald
```

**Celtic Settlements:**
```
Research Celtic place naming
Suffixes: -dun (fort), -bry (hill), -ton (settlement)
Generate: Caerdun, Brynmor, Ashton
```

**Process:**
1. Determine cultural inspiration (Germanic, Celtic, Arabic, Nordic, etc.)
2. Use WebFetch to research naming patterns from that culture
3. Generate 8-10 authentic place names
4. Present options with cultural context
5. User selects or requests more

---

**Method 2: Wikipedia Random Article Method**

Generate unique place names from random Wikipedia articles.

**Process:**
```bash
# Fetch 10 random Wikipedia articles
for i in {1..10}; do
  curl -sL "https://en.wikipedia.org/api/rest_v1/page/random/summary" | \
  python3 -c "import sys, json; data=json.load(sys.stdin); \
  print(f\"Title: {data['title']}\nExtract: {data['extract'][:200]}...\")"
  sleep 0.5
done
```

**Extract evocative terms:**
- Article: "Battle of Hastings" → Extract: Hastings
- Article: "Byzantine Empire" → Extract: Byzantine
- Article: "Coral Reef" → Extract: Coral, Reef

**Adapt into fantasy names:**
- Hastinmere (Hastings + mere/lake)
- Byzara (Byzantine inspired)
- Koralvast (Coral + vast)
- Rifport (Reef + port)

**Benefits:**
- Completely unique names
- Sound researched, not generated
- Avoid all fantasy clichés
- Evocative and memorable

---

### Place Naming Workflow

**Step 1: Determine Scope**

Ask user:
```
How many locations need names?
- Major cities: [X]
- Towns/villages: [X]
- Regions/kingdoms: [X]
- Geographic features (mountains, rivers, forests): [X]
```

**Step 2: Choose Naming Method**

```
What cultural/linguistic feel for place names?

A. Germanic (Eisenheim, Rotenburg, Schwarzwald)
B. Celtic (Caerdun, Brynmor, Lynhaven)
C. Arabic (Al-Hazan, Qalat-al-Nur, Ishdarabad)
D. Nordic (Fjordheim, Vikingstad, Holmgard)
E. Latin/Romance (Valoris, Montclair, Bellehaven)
F. Asian-inspired (Tianzhou, Hanshan, Longcheng)
G. Mixed cultures (multiple naming systems)
H. Wikipedia random method (unique evocative names)
```

**Step 3: Generate Names**

Based on choice:
- Use WebFetch to research cultural patterns OR
- Use Wikipedia random method to extract terms
- Generate 8-10 options per location type
- Present with cultural context

**Step 4: Verify Anti-Slop**

Check each name:
- ❌ Contains "Shadow", "Dark", "Storm"?
- ❌ Follows [Color]+[Noun] pattern?
- ❌ Too generic/cliché?
- ✅ Culturally consistent?
- ✅ Pronounceable?
- ✅ Memorable?

**Step 5: Document in WORLD.md**

```markdown
## Major Locations

### [City Name]
Brief description, cultural context

## Naming Conventions

All places in [region] follow [culture] patterns:
- Suffixes: -heim, -burg, -wald
- Phonetic style: Hard consonants, compound words
- Examples: Eisenheim, Rotenburg, Grünwald

When introducing new locations, maintain this pattern.
```

---

### Place Naming by Type

**Cities & Towns:**
- Research cultural suffixes
- Generate 8-10 options
- Consider: -heim, -burg, -ville, -ton, -polis, -abad

**Regions & Kingdoms:**
- Named after geography, dynasties, or culture
- Examples: The Ashen Reach, Valdorian Empire, Stormlands
- Avoid cliché adjectives (Dark, Shadow, Fallen)

**Geographic Features:**
- Mountains: The Broken Peaks, Mount Solvar, Dragonspine Range
- Rivers: River Thane, The Silverflow, Ashwater
- Forests: The Thornwood, Whispergrove, Elderwood
- Seas: The Sapphire Sea, Stormwake Ocean

**Avoid:** Excessive "Dark/Shadow/Storm" prefixes even for features.

---

### Example: Wikipedia Method for Places

**User:** "I need 5 unique city names, not standard fantasy"

**Claude:**
```
I'll use the Wikipedia random article method to create unique names.

Fetching 10 random articles...

Articles found:
1. Mionów (Polish village)
2. Battle of Hastings (historical)
3. Byzantine Empire (historical)
4. Coral Reef (natural)
5. Prudnik County (Polish region)

Extracting evocative terms: Mionów, Hastings, Byzantine, Coral, Prudnik

Adapted fantasy city names:

1. Hastinmere (Hastings + mere/lake) - Lakeside city
2. Byzara (Byzantine inspired) - Ancient capital with history
3. Koralvast (Coral + vast) - Coastal city near reefs
4. Mionwick (Mion + wick/bay) - Harbor settlement
5. Prudholm (Prud + holm/island) - Island fortress
6. Rifport (Reef + port) - Fishing village
7. Hastengard (Hasten + gard) - Fortified merchant city
8. Opolen (Opole + suffix) - Trading crossroads

Pick 5, or ask for more options generated from new articles.
```

**Why this works:** Names sound authentic and researched, avoid all AI slop patterns, completely unique.

---

## Part 3: Secondary Character Naming

**CRITICAL:** Even minor characters need authentic names, not AI slop.

### Character Naming Tiers

**Tier 1: Main Characters (Protagonists/Antagonists)**
- Individual research
- 10 options per character
- Full workflow from Section 1

**Tier 2: Supporting Characters**
- 5-8 options per character
- Same anti-slop standards
- Match cultural context

**Tier 3: Minor Recurring Characters**
- Guards, shopkeepers, servants
- Draw from pre-generated name pools
- No individual research needed

**Tier 4: Background Mentions**
- Mentioned but not appearing
- Draw from same pools as Tier 3
- NEVER generate on the fly

---

### Creating Name Pools for Minor Characters

Generate once, use throughout story.

**Process:**
1. Identify cultures in your world
2. For each culture, use WebFetch to generate:
   - 30 male names
   - 30 female names
   - 20 surnames/family names
3. Store in CHARACTERS.md
4. Draw from pools as needed while writing

**Example Pool in CHARACTERS.md:**

```markdown
## Name Pools for Minor Characters

### Valdorian Names (Germanic-inspired)

**Male Names (30):**
Gerhardt, Wilhelm, Friedrich, Heinrich, Ludwig, Albrecht, Konrad, Dietrich, Wolfram, Reinhard, Siegfried, Gunther, Helmut, Walther, Bernhard, Rolf, Klaus, Otto, Franz, Hermann, Rudolf, Ulrich, Werner, Karl, Johann, Ernst, Horst, Gottfried, Manfred, Erich

**Female Names (30):**
Katrin, Brunhilde, Gisela, Helga, Ingrid, Margarete, Hildegard, Gertrud, Hedwig, Irmgard, Adelheid, Bertha, Frieda, Lieselotte, Elke, Astrid, Brigitte, Christa, Erika, Heidi, Ilse, Karin, Marlene, Petra, Renate, Sabine, Ursula, Waltraud, Anneliese, Johanna

**Surnames (20):**
Müller, Schmidt, Wagner, Becker, Hoffmann, Schröder, Koch, Bauer, Richter, Klein, Wolf, Neumann, Schwarz, Zimmermann, Braun, Hartmann, Lange, Werner, Krause, Fischer

**Usage:** For guards, shopkeepers, servants, and background Valdorian characters. Draw as needed. Track used names to avoid repeats within same scene.
```

**Benefits:**
- Eliminates AI slop for even tiny roles
- Instant access while writing
- Cultural consistency
- Professional authenticity throughout

---

### Name Pool Generation Workflow

**Step 1: Identify Cultures**
```
Your world has:
- Valdorian culture (Germanic-inspired)
- Ishari culture (Arabic-inspired)

I'll generate name pools for both.
```

**Step 2: Generate Pools**
```
Using WebFetch with Behind the Name (Germanic filter)...
Generated 30 male, 30 female, 20 surnames for Valdorian pool.

Using WebFetch with Behind the Name (Arabic filter)...
Generated 30 male, 30 female, 20 surnames for Ishari pool.
```

**Step 3: Store in CHARACTERS.md**
```
Name pools added to CHARACTERS.md under "Name Pools for Minor Characters"
```

**Step 4: Use While Writing**
```
Need a Valdorian guard name? Draw from pool: "Gerhardt"
Need an Ishari merchant? Draw from pool: "Rashid Al-Hakim"
```

---

### Workflow for Automated Chapter Writing

When agents write chapters, add to their instructions:

```
CRITICAL NAMING RULES:

1. For NEW minor characters:
   - Draw from name pools in CHARACTERS.md
   - NEVER generate names spontaneously
   - Track used names to avoid repeats

2. For NEW locations:
   - Follow naming conventions in WORLD.md
   - Match established phonetic patterns
   - Example: If cities are "Eisenheim, Rotenburg", new city = "Grünwald" (Germanic pattern), NOT "Shadowkeep"

3. BANNED NAMES (AI Slop):
   - Characters: Kael, Elara, Lyra, Aria, Theron, Zara
   - Places: Shadowmere, Darkwood, Stormkeep, [Color]+[Noun]

4. When in doubt:
   - Use descriptive terms: "the guard", "the innkeeper"
   - User will name in revision pass
   - Better than AI slop name

5. Note any new named elements in chapter summary for user review.
```

---

### Example: Complete Naming System

**Story World:** Valdoria (Germanic) vs Ishara (Arabic), contested border

**Main Characters (Tier 1):**
- Garicus (researched, user selected)
- Solaire (researched, user selected)
- Sir Aldric (researched, user selected)
- Theron (researched, user selected)

**Supporting Characters (Tier 2):**
- Captain of guard: 5 options researched, user picks
- Merchant who reveals truth: 5 options, user picks

**Minor Characters (Tier 3-4):**
- Guards at gate: Draw from Valdorian male pool
- Shopkeepers: Draw from appropriate cultural pool
- Servants at keep: Draw from Valdorian pools

**Places:**
- Major cities: Researched Germanic patterns, 8 options each
- Villages: Draw from consistent patterns
- Regions: Wikipedia random method for uniqueness

**Result:** Zero AI slop names from protagonist to background guard, from capital city to tiny hamlet.

---

*This complete naming system is MANDATORY for all Claudespeare workflows. It covers characters (all tiers), places (all types), and methods (research, cultural patterns, Wikipedia). No element of your story should have an AI-generated name.*
