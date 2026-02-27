# AI Language Pattern Database

This database defines the language patterns commonly found in AI-generated text, with concrete replacement suggestions for each.

## Built-In Patterns

### Pattern 1: Delve/Delved/Delving
**Category:** Word choice
**Why AI-ish:** Extremely common in AI-generated text, rarely used in natural contemporary prose
**Detection:** Word forms: delve, delves, delved, delving

**Replacements:**
- "explored" (if examining something)
- "investigated" (if researching or looking into)
- "studied" (if learning or analyzing)
- "examined" (if closely inspecting)
- "dug into" (informal, for casual tone)
- Simply remove and restructure (often the verb adds no value)

**Example:**
- AI: "She delved into the ancient texts"
- Better: "She studied the ancient texts"
- Better: "She pored over the ancient texts"

---

### Pattern 2: Tapestry
**Category:** Metaphor overuse
**Why AI-ish:** AI loves "tapestry" for any complex interconnection or mixture
**Detection:** Word: tapestry (in metaphorical usage)

**Replacements:**
- "web" or "network" (if describing connections)
- "mixture" or "blend" (if describing combination)
- "array" or "collection" (if describing variety)
- Specific concrete detail (usually better than any metaphor)
- Simply remove and be direct

**Example:**
- AI: "The city was a tapestry of cultures"
- Better: "The city mixed a dozen cultures"
- Better: "Korean groceries next to Mexican taquerias next to Russian bookshops"

---

### Pattern 3: Navigate/Navigated/Navigating
**Category:** Metaphor overuse
**Why AI-ish:** AI uses "navigate" metaphorically for any challenge or process
**Detection:** Navigate/navigated/navigating in non-literal contexts (not actual physical navigation)

**Replacements:**
- "faced" or "dealt with" (if confronting challenges)
- "moved through" or "worked through" (if describing a process)
- "handled" or "managed" (if dealing with situations)
- "explored" (if discovery/investigation)
- Be specific about the actual action

**Example:**
- AI: "She navigated the complex social dynamics"
- Better: "She handled the office politics"
- Better: "She figured out who hated whom and stayed neutral"

---

### Pattern 4: Testament To
**Category:** Phrase overuse
**Why AI-ish:** AI reaches for this phrase constantly
**Detection:** Phrase: "testament to" or "a testament to"

**Replacements:**
- "proof of" or "evidence of"
- "shows" or "demonstrates"
- "reveals" or "indicates"
- Simply state the fact directly (usually strongest)
- "example of" (if appropriate)

**Example:**
- AI: "Her success was a testament to her hard work"
- Better: "Her success proved years of hard work paid off"
- Better: "She'd worked for this. It showed."

---

### Pattern 5: Juxtaposition
**Category:** Word choice
**Why AI-ish:** Overused in AI analysis and description, feels academic
**Detection:** Word: juxtaposition

**Replacements:**
- "contrast" (simpler and clearer)
- "difference" (even simpler)
- "comparison" (if actually comparing)
- "side by side" (more natural phrasing)
- Describe the actual relationship directly

**Example:**
- AI: "The juxtaposition of wealth and poverty was striking"
- Better: "The contrast between wealth and poverty was stark"
- Better: "Mansions on one block, tent cities on the next"

---

### Pattern 6: Overly Formal Academic Language
**Category:** Tone
**Why AI-ish:** AI defaults to academic formality even in creative writing

**Detection patterns:**
- Sentence starters: "Furthermore," "Moreover," "Additionally," "Nevertheless," "Consequently,"
- Academic hedging: "One might observe," "It can be seen that," "It is worth noting that"
- Narrative conclusion markers: "In conclusion," "To summarize," "In summary" (in fiction!)
- Latin phrases in casual prose: "per se," "vis-à-vis," "de facto," "ipso facto"
- Archaic formal words: "Aforementioned," "heretofore," "wherein," "whereby"

**Replacements:**
- Use simpler conjunctions: "And," "But," "So," "Yet"
- Direct statements instead of passive observation: "She saw" not "It could be observed that"
- Remove conclusion markers entirely in narrative (show, don't tell)
- Use English equivalents: "essentially" not "per se," "compared to" not "vis-à-vis"
- Modern plain language: "mentioned earlier" not "aforementioned"

**Example:**
- AI: "Moreover, one might observe that the character's behavior was, per se, a testament to her aforementioned determination."
- Better: "And her behavior showed the same determination."
- Better: "She kept going. Same stubborn drive."

---

### Pattern 7: "It's Worth Noting" Phrases
**Category:** AI hedging/meta-commentary
**Why AI-ish:** AI loves these unnecessary framing phrases

**Detection patterns:**
- "It's worth noting that"
- "It should be noted that"
- "Notably,"
- "Of note,"
- "Interestingly,"
- "It is interesting to note that"

**Replacements:**
- Simply state the fact directly (strongest option)
- "In fact," (if emphasis truly needed)
- Remove entirely (usually the phrase adds nothing)
- Let the interesting detail speak for itself

**Example:**
- AI: "It's worth noting that she had visited the house before."
- Better: "She'd been to the house before."
- Better: "In fact, she'd been to the house before."

---

### Pattern 8: Purple Prose Patterns
**Category:** Style excess
**Why AI-ish:** AI can overdo literary flourishes, piling on unnecessary drama

**Detection patterns:**
- **Excessive adjective stacking:** Three or more adjectives before a noun ("the dark, cold, forbidding, ancient castle")
- **Melodramatic adverbs:** "unutterably," "ineffably," "indescribably," "impossibly," "unbearably"
- **Overwrought metaphors (overuse):** Every emotion is "soul-crushing" or "heart-wrenching"
- **Pretentious vocabulary:** Using "domicile" instead of "house," "masticate" instead of "chew," "utilize" instead of "use"
- **Enhanced dialogue tags (every time):** "he breathed," "she whispered huskily," "he intoned," "she purred"

**Replacements:**
- **Adjectives:** Reduce to 1-2 meaningful adjectives max
- **Adverbs:** Remove or use simple adverbs ("very," "quite," "really")
- **Metaphors:** Use grounded, specific detail instead of hyperbole
- **Vocabulary:** Choose clear, natural words over impressive ones
- **Dialogue tags:** Use "said" or "asked" for 80%+ of tags; save fancy tags for rare emphasis

**Examples:**
- AI (adjectives): "The dark, menacing, ominous, looming castle"
- Better: "The dark castle" or "The castle loomed" (pick ONE descriptor)

- AI (adverbs): "She was ineffably, unutterably sad"
- Better: "She was devastated" or "She couldn't stop crying"

- AI (metaphors): "His soul-crushing, heart-wrenching, gut-punching betrayal"
- Better: "His betrayal gutted her"

- AI (vocabulary): "She proceeded to her domicile to masticate her evening repast"
- Better: "She went home to eat dinner"

- AI (dialogue tags): "Fine," she breathed huskily. "Whatever you say," he intoned darkly.
- Better: "Fine," she said. "Whatever you say."

---

## Custom Phrases

Writers can add their own overused words or phrases to watch for.

### How to Add Custom Phrases

Edit this section to add phrases you personally overuse or want to avoid:

```yaml
custom_patterns:
  - phrase: "suddenly"
    reason: "Overused as scene transition or tension marker"
    alternatives: ["without warning", "in an instant", "before she could react", "restructure to show the action directly without the adverb"]

  - phrase: "very"
    reason: "Weak intensifier that adds little"
    alternatives: ["use a stronger base word", "remove entirely", "replace with specific description"]

  - phrase: "just"
    reason: "Filler word that weakens sentences"
    alternatives: ["remove it and see if sentence is stronger", "be more specific about timing if needed"]

  - phrase: "really"
    reason: "Another weak intensifier"
    alternatives: ["use stronger word", "remove", "show the intensity through action/detail"]

  - phrase: "began to" / "started to"
    reason: "Unnecessary verb construction - just use the main verb"
    alternatives: ["use the direct verb: 'she walked' not 'she began to walk'"]
```

Add entries following this format. The detection workflow will scan for these alongside built-in patterns.

---

## Usage Notes

**Context matters:**
Not every instance is wrong. Some patterns fit certain genres (literary fiction might embrace some purple prose; academic writing in-story can use formal language). The goal is awareness, not robotic rule-following.

**Aim for natural voice:**
Replace AI patterns with language that feels human and appropriate to your story's style and genre.

**Consider your STYLE.md:**
If you've created a style profile, use those preferences to guide replacements. Formal style = different choices than casual style.

**Genre considerations:**
- Literary fiction: Can use more elevated language, but avoid AI-specific overuse
- Thriller/Mystery: Usually benefits from direct, sparse language
- Romance: Can embrace some melodrama, but watch purple prose excess
- Fantasy/Sci-fi: World-specific terms are fine; "delve" and "tapestry" are still AI-ish

**Pattern severity:**
Some patterns are nearly always wrong (delve, tapestry in metaphor). Others are context-dependent (adjective stacking okay for emphasis occasionally, but not every noun).

---

**Last Updated:** 2026-02-27

## Maintenance

This template is the global pattern database. You can:
1. Use it as-is (detection workflow reads from here)
2. Copy to your story project (`stories/{slug}/AI-PATTERNS.md`) for project-specific customization
3. Add custom patterns in the Custom Phrases section
4. Modify built-in patterns if your genre requires different treatment

The detection workflow (`/write:detect`) reads this file and applies all patterns to your prose.
