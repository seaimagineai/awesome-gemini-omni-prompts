#!/usr/bin/env python3
"""Build all README_*.md from reviewed localized copy and source excerpts.

Run from any directory: python3 scripts/build_locales.py
README.md is maintained separately; README_EN.md is its exact generated copy. No network access is required.
"""
import json
from homepage_sections import brand_section, studies_section, update_english, read, library_intro
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = [('en','EN','English'),('cn','ZH','简体中文'),('tw','ZH-TW','繁體中文'),('ja','JA','日本語'),('ko','KO','한국어'),('es','ES','Español'),('fr','FR','Français'),('de','DE','Deutsch'),('pt','PT','Português'),('it','IT','Italiano'),('ru','RU','Русский'),('id','ID','Bahasa Indonesia'),('th','TH','ไทย'),('vi','VI','Tiếng Việt'),('ar','AR','العربية')]
EN_COLLECTIONS = [
 ('Cinema and storytelling: 8 prompts','prompts/cinematic-storytelling.md'),
 ('Commerce and social media: 8 prompts','prompts/commerce-social.md'),
 ('Documentary, travel and education: 8 prompts','prompts/documentary-education.md'),
 ('Animation, music and entertainment: 8 prompts','prompts/stylized-entertainment.md'),
 ('Control, editing and extension: 10 prompts','prompts/control-editing-extension.md'),
 ('Advanced editing, camera and visual transformation: 9 prompts','prompts/advanced-editing-camera.md'),
 ('Storyboards, split screens, text and evaluation: 9 prompts','prompts/storyboard-text-evaluation.md'),
]
COPY = json.loads((ROOT/'data/locale-copy.json').read_text())
EXAMPLES = json.loads((ROOT/'data/example-prompts.json').read_text())
NAV = ' · '.join(f'[{label}](README.md)' if code=='en' else f'[{label}](README_{suffix}.md)' for code,suffix,label in LOCALES)


def build(code, suffix):
    d = COPY[code]
    additions = read('homepage-additions.json')[code]
    editorial = read('editorial-copy.json')[code]
    def neutral(text):
        for original, localized in editorial.get('neutral_replacements', {}).items():
            text = text.replace(original, localized)
        return text.replace('SeaImagine',editorial['neutral_platform'])
    source = json.loads((ROOT/f'templates/locales/README_{suffix}.json').read_text())
    prefix = '' if code=='en' else f'/{code}'
    base = 'https://seaimagine.com' + prefix
    model = f'[Gemini Omni]({base}/model/gemini-omni/) · [Gemini Omni 1.1 Flash]({base}/model/gemini-omni-1-1-flash/)'
    parts = [f'# {editorial["title"]}', NAV, studies_section(code), library_intro(code),
             '<a id="source-examples"></a>', f'## {d["examples"]}', d['image_note']]
    for i,e in enumerate(EXAMPLES,1):
        parts += [f'### {i:02d} · {d[f"example{i}"]}',f'![{d[f"example{i}"]}](assets/{e["image"]})',f'```text\n{e["prompt"]}\n```']
    parts += [neutral(source.get('after_examples','')), neutral(source.get('before_examples',''))]
    collections = source['collections'] or EN_COLLECTIONS
    assert len(collections)==7, (code,collections)
    parts += [f'## {d["collections"]}',d['language_note'],source.get('collection_table') or '\n'.join(f'- [{label}]({url})' for label,url in collections),f'## {d["dialogue_title"]}',d['dialogue_note']]
    dialogue = source['dialogue']
    if dialogue: parts += [f'```text\n{dialogue}\n```']
    if source.get('supplemental'): parts += [neutral(source['supplemental'])]
    parts += [f'## {d["reading"]}', '\n'.join(f'- [{d[k]}]({p})' for k,p in [('community','docs/community-examples.md'),('multilingual','docs/multilingual-guide.md'),('prompting','docs/prompting-guide.md'),('reference','docs/reference-videos.md')]),'<a id="brand-tools"></a>', f'## {d["start"]}', f'![{d["title"]}](assets/seaimagine-omni-hero.png)', additions['intro'], model,
              '\n'.join(f'{i}. {d[f"step{i}"]}' for i in range(1,4)), d['caution'], brand_section(code), f'[{d["workflow"]}](docs/seaimagine-workflow.md)',
              f'## {d["tools"]}',d['tools_note'], '\n'.join(f'- [{d[k]}]({base}/{p}/)' for k,p in [('create','create'),('i2v','image-to-video'),('t2v','text-to-video'),('imagegen','ai-image-generator')]), f'## {d["source_title"]}', d['source'], '[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)']
    return '\n\n'.join(parts)+'\n'


if __name__ == '__main__':
    update_english()
    for code,suffix,_ in LOCALES:
        (ROOT/f'README_{suffix}.md').write_text((ROOT/'README.md').read_text() if code=='en' else build(code,suffix))
    print(f'Built {len(LOCALES)} localized README files.')
