#!/usr/bin/env python3
"""
Apply automatic fixes to chapters based on audit findings.
Creates backups before modifying files.
"""

import re
from pathlib import Path
from datetime import datetime

# Pattern replacements
FILTER_WORD_REPLACEMENTS = {
    # Context-aware replacements for filter words
    r'\bjust\s+': '',  # Remove "just" in most cases
    r'\breally\s+': '',  # Remove "really"
    r'\bvery\s+': '',  # Remove "very"
    r'\bquite\s+': '',  # Remove "quite"
    r'\brather\s+': '',  # Remove "rather"
    r'\bsomewhat\s+': '',  # Remove "somewhat"
}

# Weak constructions to strengthen
WEAK_CONSTRUCTIONS = {
    r'\bstarted to\s+(\w+)': r'\1ed',  # "started to run" -> "ran"
    r'\bbegan to\s+(\w+)': r'\1ed',    # "began to walk" -> "walked"
    r'\btried to\s+': r'',             # "tried to" -> direct action
    r'\bmanaged to\s+': r'',           # "managed to" -> direct action
}

def backup_chapter(chapter_file: Path):
    """Create timestamped backup of chapter."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = chapter_file.with_suffix(f'.backup_{timestamp}.md')
    backup_file.write_text(chapter_file.read_text())
    return backup_file

def apply_filter_word_fixes(text: str) -> tuple[str, int]:
    """Remove unnecessary filter words."""
    fixes_made = 0
    original = text

    for pattern, replacement in FILTER_WORD_REPLACEMENTS.items():
        text, count = re.subn(pattern, replacement, text, flags=re.IGNORECASE)
        fixes_made += count

    return text, fixes_made

def apply_weak_construction_fixes(text: str) -> tuple[str, int]:
    """Strengthen weak verb constructions."""
    fixes_made = 0

    # Handle "started to X" -> "X-ed" carefully
    # We need to be smart about irregular verbs
    irregular_verbs = {
        'run': 'ran', 'begin': 'began', 'come': 'came', 'go': 'went',
        'see': 'saw', 'take': 'took', 'give': 'gave', 'speak': 'spoke',
        'break': 'broke', 'write': 'wrote', 'know': 'knew',
    }

    # For now, just remove "tried to" and "managed to" as those are always safe
    safe_patterns = {
        r'\btried to\s+': '',
        r'\bmanaged to\s+': '',
    }

    for pattern, replacement in safe_patterns.items():
        text, count = re.subn(pattern, replacement, text, flags=re.IGNORECASE)
        fixes_made += count

    return text, fixes_made

def apply_repetitive_phrase_fixes(text: str) -> tuple[str, int]:
    """Fix repetitive phrases that sound AI-generated."""
    fixes_made = 0

    # Look for "She will be X" repetition (flagged in Chapter 3)
    # Only fix if it appears more than 3 times
    pattern = r'\bShe will be\b'
    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    if len(matches) > 3:
        # Vary some instances
        def replace_func(match):
            nonlocal fixes_made
            # Keep first instance, vary others
            alternatives = [
                match.group(0),  # Original
                'She becomes',
                'She shall be',
                'She grows',
            ]
            fixes_made += 1
            return alternatives[fixes_made % len(alternatives)]

        text = re.sub(pattern, replace_func, text, flags=re.IGNORECASE)

    return text, fixes_made

def clean_chapter(chapter_file: Path, dry_run: bool = False) -> dict:
    """Apply all fixes to a chapter."""
    results = {
        'file': chapter_file.name,
        'backup': None,
        'changes': {},
        'total_fixes': 0,
    }

    # Read original content
    content = chapter_file.read_text()
    lines = content.split('\n')

    # Skip frontmatter
    frontmatter_end = 0
    if lines[0].strip() == '---':
        frontmatter_end = 1
        while frontmatter_end < len(lines) and lines[frontmatter_end].strip() != '---':
            frontmatter_end += 1
        frontmatter_end += 1

    frontmatter = '\n'.join(lines[:frontmatter_end])
    body = '\n'.join(lines[frontmatter_end:])

    # Apply fixes
    fixed_body = body

    # Filter words
    fixed_body, count = apply_filter_word_fixes(fixed_body)
    results['changes']['filter_words'] = count
    results['total_fixes'] += count

    # Weak constructions
    fixed_body, count = apply_weak_construction_fixes(fixed_body)
    results['changes']['weak_constructions'] = count
    results['total_fixes'] += count

    # Repetitive phrases
    fixed_body, count = apply_repetitive_phrase_fixes(fixed_body)
    results['changes']['repetitive_phrases'] = count
    results['total_fixes'] += count

    # Only write if changes were made and not dry run
    if results['total_fixes'] > 0 and not dry_run:
        # Create backup
        results['backup'] = backup_chapter(chapter_file)

        # Write fixed version
        fixed_content = frontmatter + '\n' + fixed_body
        chapter_file.write_text(fixed_content)

    return results

def main():
    """Main entry point."""
    story_dir = Path(__file__).parent
    chapters_dir = story_dir / "chapters"

    if not chapters_dir.exists():
        print(f"Error: Chapters directory not found: {chapters_dir}")
        return

    print("="*60)
    print("APPLYING AUTOMATIC FIXES")
    print("="*60)
    print("\nThis will:")
    print("  - Remove unnecessary filter words (just, really, very, etc.)")
    print("  - Strengthen weak constructions (tried to -> direct action)")
    print("  - Fix repetitive phrases")
    print("\nBackups will be created for all modified files.\n")

    # Process all chapters
    all_results = []

    for chapter_num in range(1, 10):
        chapter_file = chapters_dir / f"chapter-{chapter_num:02d}.md"

        if not chapter_file.exists():
            continue

        print(f"Processing Chapter {chapter_num}...")
        results = clean_chapter(chapter_file, dry_run=False)
        all_results.append(results)

        if results['total_fixes'] > 0:
            print(f"  ✓ Applied {results['total_fixes']} fixes")
            for fix_type, count in results['changes'].items():
                if count > 0:
                    print(f"    - {fix_type}: {count}")
            print(f"  Backup: {results['backup'].name}")
        else:
            print(f"  - No fixes needed")

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    total_fixes = sum(r['total_fixes'] for r in all_results)
    files_modified = len([r for r in all_results if r['total_fixes'] > 0])

    print(f"\nTotal fixes applied: {total_fixes}")
    print(f"Files modified: {files_modified}/9")

    if total_fixes > 0:
        print("\n✓ Automatic fixes complete!")
        print("\nNext steps:")
        print("  1. Review the changes")
        print("  2. Run the audit again to verify improvements")
        print("  3. Manual review for:")
        print("     - Ghibli aesthetic consistency")
        print("     - Emotional impact of key scenes")
        print("     - Fairy's alien incomprehensibility")
    else:
        print("\n✓ No automatic fixes needed - story is already clean!")

if __name__ == "__main__":
    main()
