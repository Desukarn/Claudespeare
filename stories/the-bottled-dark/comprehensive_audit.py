#!/usr/bin/env python3
"""
Comprehensive Quality Audit for "The Bottled Dark"
Checks for AI patterns, voice consistency, world-building adherence, and more.
"""

import re
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Set

@dataclass
class AuditIssue:
    """Represents a single audit issue found."""
    chapter: int
    line_num: int
    category: str
    severity: str  # "high", "medium", "low"
    issue: str
    context: str
    suggestion: str = ""

@dataclass
class AuditReport:
    """Complete audit report."""
    issues: List[AuditIssue] = field(default_factory=list)
    scores: Dict[str, float] = field(default_factory=dict)
    statistics: Dict[str, any] = field(default_factory=dict)

    def add_issue(self, issue: AuditIssue):
        self.issues.append(issue)

    def get_score(self, category: str) -> float:
        return self.scores.get(category, 0.0)

# AI PATTERN DETECTION
AI_PATTERNS = {
    # Banned words (high severity)
    'tapestry': r'\btapestry\b',
    'delve': r'\bdelve[ds]?\b',
    'enigmatic': r'\benigmatic\b',
    'juxtaposition': r'\bjuxtaposition\b',
    'dichotomy': r'\bdichotomy\b',
    'multifaceted': r'\bmultifaceted\b',
    'paradigm': r'\bparadigm\b',
    'quintessential': r'\bquintessential\b',

    # Overused AI phrases (medium severity)
    'the air hung heavy': r'the air hung heavy',
    'testament to': r'testament to',
    'serves as a reminder': r'serves as a reminder',
    'begs the question': r'begs the question',
    'it\'s worth noting': r'it\'s worth noting',
    'a sense of': r'a sense of\b',

    # Filter words (low-medium severity - track frequency)
    'just': r'\bjust\b',
    'really': r'\breally\b',
    'very': r'\bvery\b',
    'quite': r'\bquite\b',
    'rather': r'\brather\b',
    'somewhat': r'\bsomewhat\b',
    'almost': r'\balmost\b',
    'seemed': r'\bseemed?\b',
    'appeared': r'\bappeared?\b',
    'felt like': r'\bfelt like\b',

    # Crutch phrases
    'started to': r'\bstarted? to\b',
    'began to': r'\bbegan to\b',
    'decided to': r'\bdecided to\b',
    'tried to': r'\btried to\b',
    'managed to': r'\bmanaged to\b',

    # Chatbot language
    'it\'s important to': r'it\'s important to',
    'let\'s explore': r'let\'s explore',
    'dive into': r'\bdive into\b',
    'on the other hand': r'on the other hand',

    # Purple prose markers
    'myriad': r'\bmyriad\b',
    'plethora': r'\bplethora\b',
    'cacophony': r'\bcacophony\b',
    'symphony of': r'symphony of',
}

# Fancy dialogue tags to flag
FANCY_DIALOGUE_TAGS = [
    'exclaimed', 'queried', 'ejaculated', 'interjected', 'proclaimed',
    'declared', 'announced', 'stated', 'remarked', 'observed', 'noted',
    'ventured', 'offered', 'breathed', 'hissed', 'spat', 'snarled',
    'growled', 'murmured', 'whispered softly', 'said quietly',
]

# Character voices - key phrases/patterns for each
CHARACTER_VOICES = {
    'Walt': {
        'traits': ['pragmatic', 'short sentences when stressed', 'tender with Bea'],
        'avoid': ['flowery language', 'long philosophical musings'],
    },
    'Bea': {
        'traits': ['gentle', 'perceptive', 'becomes eerily poetic'],
        'transformation_marker': 'should become more alien over time',
    },
    'Fairy': {
        'traits': ['wind-chime voice', 'archaic phrasing', 'alien logic'],
        'markers': ['yessss', 'pattern', 'we/it pronoun shifts', 'harmonics'],
    }
}

# World rules to check
WORLD_RULES = {
    'transformation': [
        'gradual over weeks',
        'Bea improves too fast',
        'eyes change color',
        'wings appear',
        'doesn\'t need food/sleep',
        'craves moonlight',
    ],
    'fairy_rules': [
        'cannot lie',
        'must answer questions',
        'grants wishes with alien interpretation',
        'bound to bottle',
        'sustained on patterns/essence',
    ],
    'setting': [
        'quasi-medieval',
        'gas lamps',
        'poor district',
        'attic room',
        'Ghibli aesthetic',
    ]
}

def load_chapter(chapter_num: int, chapters_dir: Path) -> Tuple[str, List[str]]:
    """Load chapter content and return full text + lines."""
    chapter_file = chapters_dir / f"chapter-{chapter_num:02d}.md"
    if not chapter_file.exists():
        return "", []

    content = chapter_file.read_text()
    lines = content.split('\n')

    # Skip frontmatter
    if lines[0].strip() == '---':
        end_idx = 1
        while end_idx < len(lines) and lines[end_idx].strip() != '---':
            end_idx += 1
        lines = lines[end_idx+1:]

    return '\n'.join(lines), lines

def check_ai_patterns(chapter_num: int, lines: List[str], report: AuditReport):
    """Check for AI-generated patterns."""
    pattern_counts = Counter()

    for line_num, line in enumerate(lines, 1):
        line_lower = line.lower()

        for pattern_name, pattern_re in AI_PATTERNS.items():
            if re.search(pattern_re, line_lower):
                severity = 'high' if pattern_name in ['tapestry', 'delve', 'enigmatic'] else 'medium'

                report.add_issue(AuditIssue(
                    chapter=chapter_num,
                    line_num=line_num,
                    category='AI Patterns',
                    severity=severity,
                    issue=f"AI pattern detected: '{pattern_name}'",
                    context=line.strip(),
                    suggestion=f"Replace '{pattern_name}' with more natural phrasing"
                ))
                pattern_counts[pattern_name] += 1

    report.statistics['ai_patterns'] = dict(pattern_counts)

def check_dialogue_tags(chapter_num: int, lines: List[str], report: AuditReport):
    """Check for fancy dialogue tags (prefer "said")."""
    dialogue_pattern = r'"[^"]+"\s+(\w+)(?:\s+\w+)?[,.]'

    for line_num, line in enumerate(lines, 1):
        matches = re.finditer(dialogue_pattern, line)
        for match in matches:
            tag = match.group(1).lower()
            if tag in [t.split()[0] for t in FANCY_DIALOGUE_TAGS]:
                report.add_issue(AuditIssue(
                    chapter=chapter_num,
                    line_num=line_num,
                    category='Dialogue Tags',
                    severity='low',
                    issue=f"Fancy dialogue tag: '{tag}'",
                    context=line.strip(),
                    suggestion=f"Consider using 'said' instead of '{tag}'"
                ))

def check_show_vs_tell(chapter_num: int, text: str, lines: List[str], report: AuditReport):
    """Analyze filter words and telling vs showing."""
    filter_words = ['seemed', 'appeared', 'felt like', 'looked like', 'sounded like']
    filter_count = 0

    for line_num, line in enumerate(lines, 1):
        line_lower = line.lower()
        for word in filter_words:
            if word in line_lower:
                filter_count += 1
                if filter_count > 3:  # Flag if too many
                    report.add_issue(AuditIssue(
                        chapter=chapter_num,
                        line_num=line_num,
                        category='Show vs Tell',
                        severity='low',
                        issue=f"Filter word: '{word}'",
                        context=line.strip(),
                        suggestion="Consider showing directly instead of filtering"
                    ))

    report.statistics.setdefault('filter_words', {})
    report.statistics['filter_words'][f'ch{chapter_num}'] = filter_count

def check_sentence_variety(chapter_num: int, lines: List[str], report: AuditReport):
    """Check for repetitive sentence structures."""
    sentence_starts = []

    # Extract sentence starts
    text = ' '.join(lines)
    sentences = re.split(r'[.!?]+\s+', text)

    for sent in sentences:
        sent = sent.strip()
        if len(sent) > 10:
            # Get first 2-3 words
            words = sent.split()[:3]
            start = ' '.join(words).lower()
            sentence_starts.append(start)

    # Find repetitive patterns
    start_counts = Counter(sentence_starts)
    for start, count in start_counts.items():
        if count > 4:  # Same structure 5+ times
            report.add_issue(AuditIssue(
                chapter=chapter_num,
                line_num=0,
                category='Sentence Variety',
                severity='medium',
                issue=f"Repetitive sentence structure",
                context=f"'{start}...' appears {count} times",
                suggestion="Vary sentence openings for better rhythm"
            ))

    report.statistics.setdefault('sentence_variety', {})
    report.statistics['sentence_variety'][f'ch{chapter_num}'] = len(set(sentence_starts)) / max(len(sentence_starts), 1)

def check_character_voice(chapter_num: int, lines: List[str], report: AuditReport):
    """Check for character voice consistency."""
    # This is a simplified version - real check would need dialogue extraction
    walt_dialogue = []
    bea_dialogue = []
    fairy_dialogue = []

    in_dialogue = False
    current_speaker = None

    for line_num, line in enumerate(lines, 1):
        # Simple heuristic - look for "Walt said", "Bea said", etc.
        if 'walt' in line.lower() and ('said' in line.lower() or 'asked' in line.lower()):
            current_speaker = 'Walt'
        elif 'bea' in line.lower() and ('said' in line.lower() or 'asked' in line.lower()):
            current_speaker = 'Bea'
        elif 'creature' in line.lower() and ('said' in line.lower() or 'voice' in line.lower()):
            current_speaker = 'Fairy'

        # Extract quoted dialogue
        quotes = re.findall(r'"([^"]+)"', line)
        if quotes and current_speaker:
            for quote in quotes:
                if current_speaker == 'Walt':
                    walt_dialogue.append((line_num, quote))
                elif current_speaker == 'Bea':
                    bea_dialogue.append((line_num, quote))
                elif current_speaker == 'Fairy':
                    fairy_dialogue.append((line_num, quote))

    # Check fairy dialogue for required markers
    for line_num, dialogue in fairy_dialogue:
        dialogue_lower = dialogue.lower()
        if 'pattern' not in dialogue_lower and 'yessss' not in dialogue_lower and 'we' not in dialogue_lower:
            # Flag if fairy dialogue doesn't have characteristic markers
            if len(dialogue) > 20:  # Only for longer lines
                report.add_issue(AuditIssue(
                    chapter=chapter_num,
                    line_num=line_num,
                    category='Character Voice',
                    severity='low',
                    issue="Fairy dialogue missing characteristic markers",
                    context=dialogue,
                    suggestion="Add alien patterns: 'yessss', 'pattern', 'we' pronouns"
                ))

def check_pacing(chapter_num: int, text: str, report: AuditReport):
    """Check chapter pacing and length."""
    word_count = len(text.split())

    # Expected range: 2500-3500 words per chapter
    if word_count < 2000:
        report.add_issue(AuditIssue(
            chapter=chapter_num,
            line_num=0,
            category='Pacing',
            severity='medium',
            issue=f"Chapter may be too short ({word_count} words)",
            context=f"Chapter {chapter_num}",
            suggestion="Consider expanding key scenes or adding sensory detail"
        ))
    elif word_count > 4000:
        report.add_issue(AuditIssue(
            chapter=chapter_num,
            line_num=0,
            category='Pacing',
            severity='medium',
            issue=f"Chapter may be too long ({word_count} words)",
            context=f"Chapter {chapter_num}",
            suggestion="Consider tightening or splitting chapter"
        ))

    report.statistics.setdefault('word_counts', {})
    report.statistics['word_counts'][f'ch{chapter_num}'] = word_count

def calculate_scores(report: AuditReport, total_chapters: int):
    """Calculate category scores (0-10)."""

    # Count issues by category and severity
    category_issues = defaultdict(lambda: {'high': 0, 'medium': 0, 'low': 0})

    for issue in report.issues:
        category_issues[issue.category][issue.severity] += 1

    # Calculate scores (10 = perfect, 0 = major problems)
    for category in ['AI Patterns', 'Dialogue Tags', 'Show vs Tell', 'Sentence Variety', 'Character Voice', 'Pacing']:
        issues = category_issues[category]

        # Weight: high = -2, medium = -0.5, low = -0.1
        penalty = (issues['high'] * 2.0) + (issues['medium'] * 0.5) + (issues['low'] * 0.1)

        # Normalize per chapter
        penalty_per_chapter = penalty / total_chapters

        score = max(0, min(10, 10 - penalty_per_chapter))
        report.scores[category] = round(score, 1)

    # Overall score
    report.scores['overall'] = round(sum(report.scores.values()) / len(report.scores), 1)

def format_report(report: AuditReport) -> str:
    """Format the audit report as markdown."""
    output = []

    output.append("# Comprehensive Quality Audit Report")
    output.append("## The Bottled Dark\n")

    # Scores Summary
    output.append("## Quality Scores (0-10)\n")
    for category in sorted(report.scores.keys()):
        if category != 'overall':
            score = report.scores[category]
            emoji = "✅" if score >= 8 else "⚠️" if score >= 6 else "❌"
            output.append(f"- **{category}**: {score}/10 {emoji}")

    output.append(f"\n**OVERALL SCORE**: {report.scores.get('overall', 0)}/10\n")

    # Statistics
    output.append("## Statistics\n")

    if 'word_counts' in report.statistics:
        output.append("### Word Counts by Chapter")
        total_words = 0
        for ch in sorted(report.statistics['word_counts'].keys()):
            count = report.statistics['word_counts'][ch]
            total_words += count
            output.append(f"- {ch}: {count:,} words")
        output.append(f"\n**Total**: {total_words:,} words\n")

    if 'ai_patterns' in report.statistics and report.statistics['ai_patterns']:
        output.append("### AI Patterns Detected")
        for pattern, count in sorted(report.statistics['ai_patterns'].items(), key=lambda x: -x[1]):
            output.append(f"- `{pattern}`: {count} occurrences")
        output.append("")

    # Issues by Category
    output.append("## Issues by Category\n")

    issues_by_category = defaultdict(list)
    for issue in report.issues:
        issues_by_category[issue.category].append(issue)

    for category in sorted(issues_by_category.keys()):
        issues = issues_by_category[category]
        output.append(f"### {category} ({len(issues)} issues)\n")

        # Group by severity
        high = [i for i in issues if i.severity == 'high']
        medium = [i for i in issues if i.severity == 'medium']
        low = [i for i in issues if i.severity == 'low']

        if high:
            output.append(f"#### High Priority ({len(high)})\n")
            for issue in high[:10]:  # Show first 10
                output.append(f"**Chapter {issue.chapter}, Line {issue.line_num}**")
                output.append(f"- Issue: {issue.issue}")
                output.append(f"- Context: `{issue.context[:100]}`")
                if issue.suggestion:
                    output.append(f"- Suggestion: {issue.suggestion}")
                output.append("")

        if medium:
            output.append(f"#### Medium Priority ({len(medium)})\n")
            for issue in medium[:5]:  # Show first 5
                output.append(f"**Chapter {issue.chapter}, Line {issue.line_num}**")
                output.append(f"- Issue: {issue.issue}")
                output.append(f"- Context: `{issue.context[:100]}`")
                output.append("")

        if low and len(low) > 10:
            output.append(f"#### Low Priority ({len(low)})\n")
            output.append(f"*Showing first 3 of {len(low)} issues*\n")
            for issue in low[:3]:
                output.append(f"**Chapter {issue.chapter}, Line {issue.line_num}**: {issue.issue}")

    # Recommendations
    output.append("## Priority Recommendations\n")

    high_priority = [i for i in report.issues if i.severity == 'high']
    medium_priority = [i for i in report.issues if i.severity == 'medium']

    if high_priority:
        output.append("### Immediate Fixes Required")
        categories = set(i.category for i in high_priority)
        for cat in categories:
            count = len([i for i in high_priority if i.category == cat])
            output.append(f"- Fix {count} {cat} issues")

    if medium_priority:
        output.append("\n### Suggested Improvements")
        categories = set(i.category for i in medium_priority)
        for cat in categories:
            count = len([i for i in medium_priority if i.category == cat])
            output.append(f"- Review {count} {cat} issues")

    output.append("\n## Next Steps\n")
    output.append("1. Address all high-priority issues")
    output.append("2. Review medium-priority issues for quick wins")
    output.append("3. Run manual review for:")
    output.append("   - Ghibli aesthetic consistency")
    output.append("   - Emotional resonance of tender moments")
    output.append("   - Tragedy impact in final chapters")
    output.append("   - Fairy's alien nature (incomprehensible vs confusing)")

    return '\n'.join(output)

def run_audit(chapters_dir: Path, num_chapters: int = 9) -> AuditReport:
    """Run complete audit on all chapters."""
    report = AuditReport()

    print(f"Running comprehensive audit on {num_chapters} chapters...")

    for chapter_num in range(1, num_chapters + 1):
        print(f"  Auditing Chapter {chapter_num}...")

        text, lines = load_chapter(chapter_num, chapters_dir)
        if not text:
            print(f"    Warning: Chapter {chapter_num} not found")
            continue

        # Run all checks
        check_ai_patterns(chapter_num, lines, report)
        check_dialogue_tags(chapter_num, lines, report)
        check_show_vs_tell(chapter_num, text, lines, report)
        check_sentence_variety(chapter_num, lines, report)
        check_character_voice(chapter_num, lines, report)
        check_pacing(chapter_num, text, report)

    # Calculate scores
    calculate_scores(report, num_chapters)

    print(f"\nAudit complete!")
    print(f"  Total issues found: {len(report.issues)}")
    print(f"  Overall score: {report.scores.get('overall', 0)}/10")

    return report

def main():
    """Main entry point."""
    story_dir = Path(__file__).parent
    chapters_dir = story_dir / "chapters"

    if not chapters_dir.exists():
        print(f"Error: Chapters directory not found: {chapters_dir}")
        return

    # Run audit
    report = run_audit(chapters_dir)

    # Format and save report
    report_text = format_report(report)
    report_file = story_dir / "REVISION-REPORT.md"
    report_file.write_text(report_text)

    print(f"\nReport saved to: {report_file}")
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Overall Quality Score: {report.scores.get('overall', 0)}/10")
    print(f"Total Issues: {len(report.issues)}")
    print(f"  High Priority: {len([i for i in report.issues if i.severity == 'high'])}")
    print(f"  Medium Priority: {len([i for i in report.issues if i.severity == 'medium'])}")
    print(f"  Low Priority: {len([i for i in report.issues if i.severity == 'low'])}")

if __name__ == "__main__":
    main()
