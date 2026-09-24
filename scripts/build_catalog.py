#!/usr/bin/env python3
"""Build the case index, stable anchors and plain-text prompt downloads.

Recipe Markdown is the source of truth. Only marked navigation and copy links
are regenerated; existing prose and fenced code blocks are preserved.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ('cinematic-storytelling', '电影与叙事', 'Cinematic storytelling'),
    ('commerce-social', '商业广告与社交媒体', 'Commerce and social'),
    ('documentary-education', '纪录片与教育', 'Documentary and education'),
    ('stylized-entertainment', '风格化与娱乐', 'Stylized entertainment'),
    ('control-editing-extension', '多模态控制、编辑与续写', 'Multimodal control, editing and extension'),
    ('advanced-editing-camera', '进阶编辑与镜头', 'Advanced editing and camera'),
    ('storyboard-text-evaluation', '分镜、文字与评测', 'Storyboards, text and evaluation'),
]
HEADINGS = re.compile(r'^## (\d{2})\s*[｜|]\s*(.+)$', re.M)
FENCES = re.compile(r'^```[^\n]*\n(.*?)^```[ \t]*$', re.M | re.S)


def clean_generated(text):
    text = re.sub(r'<!-- catalog:toc:start -->\n.*?<!-- catalog:toc:end -->\n\n', '', text, flags=re.S)
    text = re.sub(r'<a id="case-(?:\d{2}|index)"></a>\n(?:\n)?', '', text)
    text = re.sub(r'<!-- catalog:copy:start -->\n.*?<!-- catalog:copy:end -->\n\n', '', text, flags=re.S)
    return text


def parse_cases(text):
    cases = []
    for match in HEADINGS.finditer(text):
        next_heading = re.search(r'^## ', text[match.end():], re.M)
        end = match.end() + next_heading.start() if next_heading else len(text)
        body = text[match.end():end]
        blocks = list(FENCES.finditer(body))
        if not blocks:
            raise ValueError(f'No prompt blocks: {match.group(0)}')
        cases.append((match, body, blocks))
    return cases


def build():
    categories, entries, all_prompts = [], [], []
    copy_dir = ROOT / 'prompts/copy'
    copy_dir.mkdir(exist_ok=True)
    index = [
        '# 提示词案例索引 / Prompt index',
        '[中文首页](../README_ZH.md) · [English home](../README.md)',
        '60 个完整配方，按 7 类整理。点击案例查看输入要求和完整提示词；点击 TXT 打开可下载的纯文本。多段配方保留各段顺序，使用时分段提交。',
        '60 complete recipes in 7 categories. Open a case for inputs and copyable prompts, or open TXT for a plain-text download. Submit multi-part recipes one part at a time.',
        '**案例状态 / Status:** 源库创作配方，未逐条验证生成效果；不将这些配方当作实测输出。 / Source-library practice briefs, not individually verified generated results.',
        ' · '.join(f'[{zh} / {en}](#{slug})' for slug, zh, en in CATEGORIES),
    ]
    for slug, zh, en in CATEGORIES:
        path = ROOT / 'prompts' / f'{slug}.md'
        original = path.read_text()
        text = clean_generated(original)
        cases = parse_cases(text)
        categories.append({'id': slug, 'title': zh, 'title_en': en, 'path': f'prompts/{slug}.md', 'count': len(cases)})
        toc = ['<!-- catalog:toc:start -->', '**本页案例 / Cases** · [全部 60 例 / All 60 cases](../docs/prompt-index.md)', '']
        index.extend(['', f'<a id="{slug}"></a>', '', f'## {zh} / {en} · {len(cases)}', '', '| 案例 / Case | 纯文本 / Plain text |', '| --- | --- |'])
        all_prompts.append(f'CATEGORY: {zh} / {en}')
        additions = []
        for match, body, blocks in cases:
            number, title = match.groups()
            case_id, anchor = f'{slug}-{number}', f'case-{number}'
            copy_path = f'prompts/copy/{case_id}.txt'
            metadata = next((line for line in body[:blocks[0].start()].splitlines() if line.startswith('**模式') or line.startswith('**Mode:')), '')
            entries.append({'metadata': metadata, 'id': case_id, 'category': slug, 'title': title, 'path': f'prompts/{slug}.md', 'anchor': anchor, 'copy_path': copy_path, 'block_count': len(blocks)})
            if len(blocks) == 1:
                plain = blocks[0].group(1)
            else:
                chunks = [title]
                prior_end = 0
                for i, block in enumerate(blocks, 1):
                    labels = re.findall(r'^###\s+(.+)$', body[prior_end:block.start()], re.M)
                    label = labels[-1] if labels else f'Part {i}'
                    chunks.append(f'=== {i}/{len(blocks)}: {label} ===\n\n{block.group(1)}')
                    prior_end = block.end()
                plain = '\n\n'.join(chunks)
            (ROOT / copy_path).write_text(plain.rstrip('\n') + '\n')
            all_prompts.append(f'CASE {number}: {title}\n{metadata}\n\n{plain.rstrip()}')
            toc.append(f'- [{number} · {title}](#{anchor}) · [TXT](copy/{case_id}.txt)')
            safe_title = title.replace('|', '\\|')
            index.append(f'| [{number} · {safe_title}](../prompts/{slug}.md#{anchor}) | [TXT](../{copy_path}) |')
            copy_link = f'\n\n<!-- catalog:copy:start -->\n[复制全文 / Download TXT](copy/{case_id}.txt) · [本页索引 / Case index](#case-index)\n<!-- catalog:copy:end -->'
            additions.append((match.end(), copy_link))
            additions.append((match.start(), f'<a id="{anchor}"></a>\n\n'))
        for position, addition in sorted(additions, reverse=True):
            text = text[:position] + addition + text[position:]
        toc.extend(['<!-- catalog:toc:end -->', ''])
        start = text.index('<a id="case-')
        text = text[:start] + '\n'.join(['<a id="case-index"></a>', '', *toc]) + '\n' + text[start:]
        if FENCES.findall(original) != FENCES.findall(text):
            raise ValueError(f'Prompt blocks changed: {path}')
        path.write_text(text)
    if len(entries) != 60 or len({row['id'] for row in entries}) != 60:
        raise ValueError('Expected exactly 60 unique cases')
    (ROOT / 'data/prompt-catalog.json').write_text(json.dumps({'categories': categories, 'cases': entries}, ensure_ascii=False, indent=2) + '\n')
    (copy_dir / 'all-prompts.txt').write_text(('\n\n' + '=' * 72 + '\n\n').join(all_prompts) + '\n')
    index.insert(6, '[下载全部 60 例 / Download all 60 recipes](../prompts/copy/all-prompts.txt)')
    (ROOT / 'docs/prompt-index.md').write_text('\n\n'.join(index[:6]) + '\n\n' + '\n'.join(index[6:]) + '\n')
    print(f'Built {len(entries)} cases in {len(categories)} categories; {sum(row["block_count"] for row in entries)} prompt blocks.')


if __name__ == '__main__':
    build()
