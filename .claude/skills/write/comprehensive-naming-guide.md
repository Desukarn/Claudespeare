# Comprehensive Naming Guide - Anti-AI-Slop for ALL Story Elements

## Overview

This guide expands naming best practices beyond main characters to cover:
- **Character naming tiers** (protagonists to background mentions)
- **Place naming systems** (cities, regions, geographic features)
- **Internal consistency** (cultural and phonetic patterns)
- **Wikipedia random article method** (creative inspiration)
- **Anti-slop verification** (avoiding clichés and AI patterns)

---

## Part A: Character Naming Tiers

### Tier 1: Protagonists & Major Characters

**Who:** Main characters, POV characters, central antagonists

**Process:**
1. Use WebFetch to access Behind the Name or Fantasy Name Generators
2. Generate 10 options per character
3. Consider name meaning and cultural fit
4. Present options to user with context
5. User selects or requests regeneration

**Time investment:** 2-3 minutes per character

**Why:** These names appear hundreds of times. They need to be memorable, culturally appropriate, and free of AI slop patterns.

**Example workflow:**
```
User: "I need a name for my protagonist, a Celtic warrior woman"

Claude: "I'll fetch authentic Celtic female names. Hold on..."

[Uses WebFetch: https://www.behindthename.com/random/ with Celtic filter]

Here are 10 authentic Celtic names with meanings:

1. Brighid (strength, power, vigor)
2. Aoife (beautiful, radiant)
3. Niamh (brightness, radiance)
4. Maeve (she who intoxicates)
5. Rhiannon (great queen)
6. Deirdre (sorrowful, sad one)
7. Aisling (dream, vision)
8. Fionnuala (white shoulder)
9. Siobhan (God is gracious)
10. Caitríona (pure)

Pick a number (1-10) or ask for more options.
```

---

### Tier 2: Supporting Characters

**Who:** Major supporting roles, recurring characters, important NPCs

**Process:**
1. Use WebFetch with appropriate generator
2. Generate 5-8 options per character
3. Match cultural context to main characters
4. User selects or requests more

**Time investment:** 1-2 minutes per character

**Why:** These characters appear regularly and need distinct, memorable names that don't blend together.

---

### Tier 3: Minor Recurring Characters

**Who:** Guards with names, shopkeepers, servants, minor plot characters

**Process:**
1. Generate cultural name pools (see below)
2. Draw from appropriate pool as needed
3. 30+ names per cultural group
4. No repeated consultation needed

**Time investment:** 5 minutes per cultural pool (reusable)

**Why:** Even minor characters deserve authentic names, but individual research isn't practical. Pools prevent AI slop while maintaining efficiency.

---

### Tier 4: Background & Mentioned Characters

**Who:** Characters mentioned but not appearing, crowd members, fleeting references

**Process:**
- Draw from same cultural name pools as Tier 3
- Or use simple patronymic/descriptive patterns ("the baker", "Jon's son")
- NEVER use AI-generated names even for these

**Time investment:** Seconds (draw from existing pool)

**Why:** Even tiny roles contribute to world authenticity. A single "Kael the guard" ruins immersion.

---

## Part B: Place Naming Philosophy

### Core Principles

**1. Internal Consistency**
- Places in the same culture share phonetic patterns
- Conquered regions show mixed naming (layers of history)
- Geographic features influence naming conventions

**2. Real-World Inspiration (Not Copying)**
- Study real toponymy (place name origins)
- Adapt patterns, don't copy names directly
- Mix cultural influences thoughtfully

**3. Avoid Fantasy Clichés**
- ❌ BANNED: Shadowmere, Darkwood, Stormkeep
- ❌ Pattern: [Color] + [Generic Noun] = "Redwood", "Blackwater"
- ❌ Pattern: [Adjective] + [Common Noun] = "Dark Tower", "Lost City"
- ❌ Excessive apostrophes: "K'nar'th'ul"
- ❌ Unpronounceable consonant clusters: "Xrthgzk"

**4. History Implied**
- Good place names suggest history without explaining it
- "Oldgate" implies there was a new gate
- "King's Rest" suggests a burial or death
- "Forgeholm" indicates metalworking heritage

**5. Pronounceability Test**
- Say it out loud three times
- Can you remember it 5 minutes later?
- Could you spell it after hearing it once?
- If no to any: revise

---

## Part C: Place Naming by Type

### Cities & Towns

**Research Method:**
1. Determine cultural inspiration (Germanic, Celtic, Arabic, etc.)
2. Use WebFetch to research real-world naming patterns from that culture
3. Generate 8-10 options using appropriate suffixes and roots
4. User selects or requests more

**Common Suffixes by Culture:**
- **Germanic:** -heim (home), -burg (fortress), -wald (forest), -dorf (village), -hof (court)
- **Celtic:** -dun (fort), -bry (hill), -mor (great), -lyn (lake), -ton (settlement)
- **Arabic:** -abad (city), -istan (land), -al- prefix (the), -dar (house)
- **Asian (Chinese):** -zhou (region), -cheng (city), -shan (mountain), -hu (lake)
- **Latin/Romance:** -polis (city), -ville (town), -mont (mountain), -vale (valley)
- **Nordic:** -fjord (fjord), -vik (bay), -by (village), -land (land), -holm (island)

**Example - Germanic-Inspired City Names:**
```
Roots: Eisen (iron), Rot (red), Grün (green), Silber (silver), Schwarz (black)
Suffixes: -heim, -burg, -wald

Generated names:
1. Eisenheim (Iron home)
2. Rotenburg (Red fortress)
3. Grünwald (Green forest)
4. Silberburg (Silver fortress)
5. Schwarzheim (Black home)
6. Grauhof (Gray court)
7. Neustadt (New city)
8. Altenburg (Old fortress)
```

---

### Regions & Kingdoms

**Naming Approaches:**

**A. Geographic Features:**
- The Ashen Reach (from ash/destruction)
- The Frozen Marches (border territory)
- The Verdant Coast (green coastline)

**B. Historical/Dynastic:**
- Karelian Empire (named after founder Karel)
- The Theyrian Kingdoms (from Theyr dynasty)
- New Valdoria (colonizers from Valdor)

**C. Cultural/Descriptive:**
- The Sunlit Realms (perpetual summer)
- Stormlands (frequent tempests)
- The Silent Wastes (desolate, uninhabited)

**Process:**
1. Consider geography, history, and culture
2. Generate 5-8 options
3. Check for cliché patterns (avoid "Shadow-" and "Dark-")
4. User selects

---

### Geographic Features

**Mountains:**
- Use local language patterns
- Named after gods, events, or appearance
- Examples: The Broken Peaks, Dragonspine Range, Mount Solvar

**Rivers:**
- Often oldest names in a region (pre-conquest)
- Simple, flowing sounds
- Examples: River Thane, The Silverflow, Ashwater

**Forests:**
- Tied to legend or appearance
- Avoid "Dark" and "Shadow" prefix
- Examples: The Thornwood, Whispergrove, Elderwood

**Seas/Oceans:**
- Named by first explorers or for qualities
- Grand, memorable
- Examples: The Sapphire Sea, Stormwake Ocean, The Endless Blue

---

## Part D: Wikipedia Random Article Method

This method generates creative, non-clichéd place names by extracting evocative words from random Wikipedia articles.

### Step-by-Step Process

**1. Fetch Random Articles**
Use Bash to fetch 10 random Wikipedia articles:
```bash
for i in {1..10}; do
  curl -sL "https://en.wikipedia.org/api/rest_v1/page/random/summary" | \
  python3 -c "import sys, json; data=json.load(sys.stdin); print(f\"Title: {data['title']}\nExtract: {data['extract'][:200]}...\n\")"
  sleep 0.5
done
```

**2. Extract Evocative Terms**
From each article, identify:
- Place names
- Historical terms
- Unique words
- Interesting syllables
- Cultural references

**3. Adapt and Combine**
- Take syllables from multiple articles
- Combine elements that sound good together
- Adjust spelling for your world's style
- Add appropriate suffixes from cultural patterns

**4. Test and Refine**
- Say it out loud
- Check for accidental meanings
- Ensure pronounceability
- Verify it fits your world's established patterns

---

### Wikipedia Method Example

**Articles Fetched:**
1. "Mionów" (Polish village)
2. "Gibberula ronchinorum" (sea snail species)
3. "Battle of Hastings" (historical battle)
4. "Byzantine Empire" (historical empire)
5. "Coral Reef" (natural formation)
6. "Tamago kake gohan" (Japanese dish)
7. "Sharon Dede Padi" (Ghanaian painter)
8. "Momoko Ando" (Japanese director)
9. "Prudnik County" (Polish region)
10. "Opole Voivodeship" (Polish province)

**Extracted Evocative Terms:**
- Mionów, Hastings, Byzantine, Coral, Reef, Opole, Prudnik, Voivodeship
- Syllables: -mion, -pol, -hast, -reef, -byz, -nik

**Adapted Fantasy Names:**

**Cities:**
1. **Hastinmere** (Hastings + mere/lake) - Coastal city
2. **Byzara** (Byzantine inspired) - Ancient capital
3. **Opolen** (Opole + -en suffix) - Trading town
4. **Mionwick** (Mionów + wick/bay) - Harbor settlement
5. **Prudholm** (Prudnik + holm/island) - Island fortress
6. **Koralvast** (Coral + vast) - Port city near reefs
7. **Rifport** (Reef + port) - Fishing village
8. **Hastgard** (Hast + gard/garden) - Agricultural center

**Regions:**
1. **The Byzantine Reach** (Byzantine + reach) - Historical empire ruins
2. **Mionveld** (Mion + veld/field) - Open plains
3. **The Coral Marches** - Tropical border region

**Why This Works:**
- Names feel researched, not generated
- Unexpected combinations avoid clichés
- Real-world roots provide authenticity
- Fully original (no direct copying)

---

## Part E: Cultural Naming Systems

### Creating Internal Consistency

When building a world with multiple cultures, establish phonetic rules for each.

**Example: Two Cultures in One World**

**Culture A: The Valdorians (Germanic-inspired)**
- Phonetic pattern: Hard consonants, compound words
- Suffixes: -heim, -burg, -wald, -hof
- Examples: Eisenheim, Rotenburg, Schwarzwald
- Character names: Gerhardt, Wilhelm, Katrin, Brunhilde

**Culture B: The Ishari (Arabic-inspired)**
- Phonetic pattern: Flowing sounds, -al prefix common
- Suffixes: -abad, -dar, -al-
- Examples: Al-Hazan, Ishdarabad, Qalat-al-Nur
- Character names: Rashid, Zahra, Malik, Layla

**Mixed/Conquered Territory:**
- Original Ishari name: Qalat-al-Nur (Castle of Light)
- After Valdorian conquest: Lichtburg (Light fortress)
- Mixed name showing both: Nuremberg (Nur + berg)

**This creates believable history:**
- Older maps show Ishari names
- New maps show Valdorian names
- Common speech uses mixed names
- Scholars argue over "proper" names

---

### Constructed Language Approach (Optional)

For deeper worldbuilding, create simple phonetic rules:

**Example: Fantasy Culture "Aethran"**

**Phonetic Rules:**
- All names end in vowels or -n, -l, -r
- Consonant clusters limited to two max
- Use ae, ei, ao diphthongs
- Avoid j, k, x, z sounds

**Generated Names Following Rules:**
- Cities: Aethran, Veilor, Caelin, Morael
- People: Naerin, Lia, Theron, Eilara
- Regions: The Aethran Vale, Veil Coast

**Consistency benefit:** All names immediately identifiable as from this culture.

---

## Part F: Anti-Slop Verification for Places

### Banned Place Name Patterns

**❌ Prefix/Suffix Combinations to Avoid:**
- Shadow + [anything]: Shadowmere, Shadowkeep, Shadowfen
- Dark + [anything]: Darkwood, Darkhaven, Darkwater
- Storm + [anything]: Stormkeep, Stormreach, Stormhaven
- Dragon + [anything]: Dragonspire, Dragonkeep (unless literal dragon)
- Frost/Ice + [noun]: Frostholm, Icehaven (unless arctic setting)
- Blood + [noun]: Bloodstone, Bloodmoor (overused in fantasy)

**❌ Generic Fantasy Patterns:**
- [Color] + [Landscape]: Redwood, Blackwater, Greenmoor
- [Weather] + [Structure]: Raincourt, Windtower
- [Material] + [Building]: Irongate, Stonewall
- The [Adjective] [Noun]: The Fallen Kingdom, The Lost City

**❌ Excessive Fantasy Markers:**
- Too many apostrophes: D'ren'al'thur
- Unpronounceable: Xrthgzk'nal
- Random capitals: DarkHaven, StormKeep

**✅ Good Place Names:**
- Imply history: "Ashmark" (something burned here)
- Cultural specificity: "Eisenheim" (clearly Germanic)
- Pronounceable: "Koralis" (easy to say and spell)
- Memorable: "The Singing Stones" (evocative image)
- Unexpected: "Whitefall" (white waterfall, not snow)

---

### Testing Place Names - Checklist

Before finalizing a place name, test:

1. **Say it out loud 3 times** - Does it flow naturally?
2. **Spell it from memory** - Can you remember the spelling?
3. **Google it** - Does it accidentally match a real place/brand?
4. **Check cliché list** - Is it on the banned patterns list?
5. **Cultural fit** - Does it match established naming conventions?
6. **Pronounceability** - Can readers say it without a guide?
7. **Memorability** - Will readers remember it after first mention?

**If any answer is "no":** Revise or generate new options.

---

## Part G: Name Pools for Minor Characters

### Creating Cultural Name Pools

Generate once, use many times for minor characters.

**Process:**
1. Identify cultures in your world
2. For each culture, use WebFetch to generate 30+ male names, 30+ female names, 20+ surnames
3. Store in CHARACTERS.md
4. Draw from pools as needed

**Example Pool Structure in CHARACTERS.md:**

```markdown
## Name Pools for Minor Characters

### Valdorian Names (Germanic-inspired)

**Male Names (30):**
Gerhardt, Wilhelm, Friedrich, Heinrich, Ludwig, Albrecht, Konrad, Dietrich, Wolfram, Reinhard, Siegfried, Gunther, Helmut, Walther, Bernhard, Rolf, Klaus, Otto, Franz, Hermann, Rudolf, Ulrich, Werner, Karl, Johann, Ernst, Horst, Gottfried, Manfred, Erich

**Female Names (30):**
Katrin, Brunhilde, Gisela, Helga, Ingrid, Margarete, Hildegard, Gertrud, Hedwig, Irmgard, Adelheid, Bertha, Frieda, Lieselotte, Elke, Astrid, Brigitte, Christa, Erika, Heidi, Ilse, Karin, Marlene, Petra, Renate, Sabine, Ursula, Waltraud, Anneliese, Johanna

**Surnames (20):**
Müller, Schmidt, Wagner, Becker, Hoffmann, Schröder, Koch, Bauer, Richter, Klein, Wolf, Neumann, Schwarz, Zimmermann, Braun, Hartmann, Lange, Werner, Krause, Fischer

**Usage:** For guards, shopkeepers, servants, and background Valdorian characters. Draw as needed. Track used names to avoid repeats in same scene.

### Ishari Names (Arabic-inspired)

**Male Names (30):**
Rashid, Malik, Khalid, Omar, Tariq, Hassan, Ibrahim, Yusuf, Jamal, Karim, Faisal, Samir, Zaid, Nasir, Hakim, Majid, Nabil, Rafi, Salim, Walid, Zayn, Adil, Fahim, Hamza, Idris, Latif, Marwan, Qasim, Rafiq, Sharif

**Female Names (30):**
Zahra, Layla, Amina, Fatima, Nadia, Yasmin, Samira, Leila, Aisha, Maryam, Salma, Zainab, Hana, Rania, Soraya, Jamila, Karima, Nabila, Rasha, Safiya, Wafa, Aziza, Basma, Dalia, Farah, Habiba, Inaya, Khadija, Lamis, Nawal

**Surnames/Family Names (20):**
Al-Rashid, Ibn-Malik, Al-Hakim, Ibn-Tariq, Al-Nazari, Ibn-Hassan, Al-Aziz, Ibn-Khalid, Al-Mansur, Ibn-Yusuf, Al-Fahim, Ibn-Karim, Al-Qadir, Ibn-Jamal, Al-Rahim, Ibn-Omar, Al-Sadiq, Ibn-Walid, Al-Zahir, Ibn-Faisal
```

**Benefits:**
- No AI slop names for even tiny roles
- Cultural consistency maintained
- Instant access when writing
- Can track which names used to avoid repeats

---

## Part H: Integration with Writing Workflows

### In YOLO Mode (Quick Setup)

**After main character naming (Step 2.2), add:**

**Step 2.3: Place and Location Naming**

Ask user:
```
What cultural/linguistic feel do you want for place names?

Options:
A. Germanic (Eisenheim, Rotenburg, Schwarzwald)
B. Celtic (Caerdun, Brynmor, Lynhaven)
C. Arabic (Al-Hazan, Qalat-al-Nur, Ishdarabad)
D. Nordic (Fjordheim, Vikingstad, Holmgard)
E. Latin/Romance (Valoris, Montclair, Bellehaven)
F. Asian-inspired (Tianzhou, Hanshan, Longcheng)
G. Mixed cultures
H. Wikipedia random method (I'll generate unique names from random articles)
```

Based on user choice:
1. Generate 8-10 city/town names
2. Generate 3-5 region names
3. Generate 2-3 major geographic feature names
4. Present options
5. User selects or requests more
6. Document in WORLD.md

**Step 2.4: Generate Minor Character Name Pools**

```
I'll create name pools for minor characters to prevent AI slop names.

Generating 30 male, 30 female, 20 surname options for [culture]...
[Uses WebFetch to appropriate generator]

These pools will be stored in CHARACTERS.md so you can draw names for guards, shopkeepers, servants, etc. as you write without needing to research each one.
```

---

### In In-Depth Mode

**During worldbuilding phase:**
- Full place naming session
- Multiple cultural naming systems if applicable
- Naming convention documentation
- Etymology notes for major locations

**During character creation:**
- Individual research for all named characters (Tier 1-3)
- Generate pools for background characters (Tier 4)
- Cultural matching to established world

---

### For Automated Chapter Writing

**When agents are spawned to write chapters:**

Add to their instructions:
```
CRITICAL NAMING RULES:

1. For NEW locations: Reference WORLD.md naming conventions. If introducing a new place, follow established phonetic patterns. EXAMPLE: If existing cities are "Eisenheim" and "Rotenburg", new city should follow Germanic pattern like "Grünwald", NOT "Shadowkeep".

2. For MINOR characters: Draw from name pools in CHARACTERS.md. NEVER generate names spontaneously.

3. BANNED: All AI slop patterns (Kael, Elara, Shadowmere, Darkwood, etc.)

4. If you MUST introduce a named element not in existing docs:
   - Follow established cultural patterns exactly
   - Note it in your summary for user review
   - User will verify authenticity in revision pass

5. When in doubt: Use descriptive terms instead of names ("the guard", "the innkeeper", "the old woman") and let user name them in revision.
```

---

## Part I: Quick Reference Tables

### Common Suffixes by Culture

| Culture | City/Town | Fort/Castle | Forest | Mountain | Water |
|---------|-----------|-------------|--------|----------|-------|
| Germanic | -heim, -stadt | -burg | -wald | -berg | -see, -bach |
| Celtic | -ton, -dun | -caer, -dun | -lyn | -ben, -tor | -mor, -lynn |
| Arabic | -abad, -dar | -qalat | -ghar | -jabal | -bahr |
| Nordic | -by, -stad | -borg | -skog | -fjell | -fjord, -vik |
| Latin | -ville, -polis | -castrum | -silva | -mons | -mare, -flumen |
| Asian | -zhou, -cheng | -cheng | -lin | -shan | -hu, -jiang |

---

### Phonetic Pattern Examples

| Culture Type | Common Sounds | Avoid |
|--------------|---------------|-------|
| Germanic | Hard consonants, compounds | Soft flowing sounds |
| Celtic | Soft consonants, diphthongs | Harsh clusters |
| Arabic | Flowing, -al prefix | Hard K/G sounds |
| Nordic | -j, -k, double consonants | Soft vowel endings |
| Latin | Clear vowels, -us/-is/-um | Consonant clusters |
| Asian | Tonal simplicity, -ng | -l endings |

---

### Real-World Inspiration Sources

**For City Names:**
- German towns: Rothenburg, Würzburg, Heidelberg patterns
- Celtic sites: Caernarfon, Aberystwyth, Dundee patterns
- Arabic cities: Baghdad, Samarkand, Al-Qayrawan patterns
- Nordic towns: Reykjavik, Trondheim, Uppsala patterns

**For Character Names:**
- Behind the Name: Historical filters by culture and era
- Medieval census records: Authentic period names
- Historical figure databases: Real names from target era

**Don't copy directly - adapt the patterns**

---

## Part J: Example Workflows

### Example 1: Creating a Germanic-Inspired Fantasy Region

**User:** "I want a Germanic-feel fantasy kingdom with 5 major cities"

**Claude:**

1. **Establish naming conventions**
```
I'll create Germanic-inspired city names using authentic patterns:
- Roots from German geography/materials
- Suffixes: -heim (home), -burg (fortress), -wald (forest)
- Phonetic style: Hard consonants, compound words
```

2. **Generate options**
```
Here are 8 city name options for your kingdom:

1. Eisenheim (Iron-home, suggests metalworking)
2. Rotenburg (Red fortress, perhaps red stone/clay)
3. Grünwald (Green forest, surrounded by woods)
4. Steinburg (Stone fortress, mountain stronghold)
5. Neustadt (New city, recent founding)
6. Altdorf (Old village, ancient settlement)
7. Silberhof (Silver court, noble/wealthy)
8. Grauhaven (Gray haven, port city)

Pick 5, or ask for more options.
```

3. **User selects:** "I'll take 1, 2, 3, 5, and 8"

4. **Document in WORLD.md**
```markdown
## Major Cities

### Eisenheim
Iron-working capital, known for master smiths and weapons manufacturing.

### Rotenburg
Fortress city built on red stone cliffs overlooking the river.

### Grünwald
Trading hub surrounded by vast forests, lumber and hunting economy.

### Neustadt
Recently founded city, modern architecture, refugee population.

### Grauhaven
Major port on the Gray Sea, international trade center.

## Naming Conventions

All cities in this kingdom follow Germanic patterns:
- Compound words (root + suffix)
- Suffixes: -heim, -burg, -wald, -haven, -stadt
- Hard consonants, practical descriptors
- Names reflect geography or economy

When introducing new locations, maintain this pattern.
```

---

### Example 2: Wikipedia Random Method for Unique Names

**User:** "I want truly unique place names, not just Germanic variants"

**Claude:**

1. **Fetch 10 random Wikipedia articles**
```
Fetching random articles for evocative inspiration...

Articles:
1. Mionów (Polish village)
2. Battle of Hastings
3. Byzantine Empire
4. Coral Reef systems
5. Prudnik County
6. Opole Voivodeship
7. Tamago kake gohan
8. Sharon Dede Padi
9. Gibberula ronchinorum
10. Momoko Ando
```

2. **Extract and adapt**
```
Evocative terms extracted:
- Mionów, Hastings, Byzantine, Coral, Prudnik, Opole
- Syllables: -mion, -hast, -byz, -pol, -reef, -nik

Adapted fantasy names:

Cities:
1. Hastinmere (Hastings + mere) - Lake city
2. Byzara (Byzantine inspired) - Ancient capital
3. Opolen (Opole + suffix) - Trading town
4. Mionwick (Mion + wick) - Harbor
5. Koralvast (Coral + vast) - Coastal city near reefs
6. Prudholm (Prud + holm) - Island fortress
7. Rifport (Reef + port) - Fishing village
8. Hastengard (Hasten + gard) - Fortified city

Regions:
1. The Byzantine Reach - Historical empire ruins
2. Mionveld - Open plains
3. The Coral Marches - Tropical borderland

Pick 5-6 for your world, or I can generate more from new articles.
```

3. **User:** "I'll take Byzara, Koralvast, Rifport, Hastinmere, and The Byzantine Reach"

**Benefits:** Names that sound researched and authentic but are fully original, avoiding all fantasy clichés.

---

## Part K: Troubleshooting Common Issues

### Problem: Names Sound Too Generic

**Solution:** Add specific cultural markers
- Generic: "Rivertown"
- Specific: "Flussheim" (German), "Avonbury" (Celtic), "Nahrabad" (Arabic)

---

### Problem: Can't Remember Names While Writing

**Solution:** Names are too complex
- Test: Say it 3 times, look away, spell from memory
- If you can't, simplify or choose different name
- Good: "Byzara" (easy)
- Bad: "Byzantarolos" (too long)

---

### Problem: Too Many Similar Names

**Solution:** Vary starting consonants and syllable count
- Bad: Kael, Kalen, Kara, Kira (all K-, 2 syllables)
- Good: Theron, Lysa, Marcus, Nia (varied starts, varied length)

---

### Problem: Mixing Cultural Patterns Inconsistently

**Solution:** Document which cultures exist where
- Map culture to geography
- Keep naming conventions in separate sections
- Mixed zones should show clear historical reason
- Example: Border town has mixed Germanic-Celtic names (conquest history)

---

### Problem: Wikipedia Method Gives Unusable Articles

**Solution:** Fetch 15-20 articles instead of 10
- You only need 5-6 good evocative terms
- Scientific articles often have interesting syllables
- Historical articles are especially valuable
- Discard articles with no evocative terms

---

## Part L: Complete Example - Building a Multi-Cultural World

**World:** Two rival kingdoms (Germanic vs Arabic-inspired) with a contested border region

### Step 1: Establish Both Naming Systems

**Kingdom A: Valdoria (Germanic)**
- Phonetics: Hard consonants, compounds
- Suffixes: -heim, -burg, -wald
- Cities: Eisenheim, Rotenburg, Schwarzwald
- People: Gerhardt, Katrin, Wilhelm

**Kingdom B: Ishara (Arabic)**
- Phonetics: Flowing, -al prefix
- Suffixes: -abad, -dar, -al
- Cities: Al-Hazan, Qalat-al-Nur, Ishdarabad
- People: Rashid, Zahra, Malik

### Step 2: Create Border Region with Mixed Names

**The Contested Marches:**
- Original Ishari settlements with Valdorian renaming
- Shows conquest history

| Original (Ishari) | Valdorian Name | Common Name |
|-------------------|----------------|-------------|
| Qalat-al-Nur | Lichtburg | Nuremberg |
| Safina-dar | Hafenstadt | Safhaven |
| Al-Qamar | Mondheim | Mondheim |

**Result:** Border region names show cultural tension through toponymy. Old maps vs new maps become plot device.

### Step 3: Generate Character Name Pools for Each Culture

**Valdorian Pool:** 30 male, 30 female, 20 surnames (Germanic)
**Ishari Pool:** 30 male, 30 female, 20 surnames (Arabic)
**Mixed Border Pool:** Names from both cultures

### Step 4: Document All in WORLD.md

```markdown
## Naming Conventions

### Valdorian Naming (Germanic-Inspired)
[Full patterns, examples, character pools]

### Ishari Naming (Arabic-Inspired)
[Full patterns, examples, character pools]

### Border Region - The Contested Marches
Shows historical conquest through mixed toponymy:
- Ishari settlements renamed by Valdorian conquerors
- Old names persist in common speech
- Political tension reflected in which name used
[Examples, cultural notes]
```

**Benefits:**
- Rich cultural detail through naming alone
- Plot opportunities (which name character uses reveals allegiance)
- Consistent patterns readers can learn
- No AI slop anywhere

---

## Summary: The Complete Anti-Slop Naming System

**For Characters:**
- Tier 1 (protagonists): Individual research, 10 options each
- Tier 2 (supporting): 5-8 options each
- Tier 3-4 (minor/background): Draw from cultural name pools

**For Places:**
- Cities/towns: 8-10 options, culturally appropriate suffixes
- Regions: 3-5 options, historically meaningful
- Features: Named with cultural patterns or Wikipedia method

**Methods:**
- WebFetch + name generators (Behind the Name, Fantasy Name Generators)
- Wikipedia random article method (evocative term extraction)
- Cultural pattern systems (documented conventions)
- Name pool generation (bulk authentic names)

**Verification:**
- Say it out loud test
- Pronounceability check
- Cliché/AI slop pattern check
- Cultural consistency check
- Memorability test

**Documentation:**
- CHARACTERS.md: Character names + pools
- WORLD.md: Place names + naming conventions
- Reference during all writing

**Result:** Complete elimination of AI slop names at every level, from protagonist to background mentions, from capital cities to tiny villages. Professional authenticity throughout.
