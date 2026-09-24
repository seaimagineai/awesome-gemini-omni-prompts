#!/usr/bin/env python3
"""Build a browsable prompt catalogue for experienced users in all 15 locales."""
import json
import re
from pathlib import Path
from homepage_sections import brand_section, read, update_workflow

ROOT = Path(__file__).resolve().parents[1]
LOCALES = [('en','EN','English'),('cn','ZH','简体中文'),('tw','ZH-TW','繁體中文'),('ja','JA','日本語'),('ko','KO','한국어'),('es','ES','Español'),('fr','FR','Français'),('de','DE','Deutsch'),('pt','PT','Português'),('it','IT','Italiano'),('ru','RU','Русский'),('id','ID','Bahasa Indonesia'),('th','TH','ไทย'),('vi','VI','Tiếng Việt'),('ar','AR','العربية')]
PATHS = ['cinematic-storytelling','commerce-social','documentary-education','stylized-entertainment','control-editing-extension','advanced-editing-camera','storyboard-text-evaluation']
EN_COLLECTIONS = ['Cinema and storytelling','Commerce and social media','Documentary, travel and education','Animation, music and entertainment','Control, editing and extension','Advanced editing, camera and visual transformation','Storyboards, text and evaluation']
COUNTS = [8,8,8,8,10,9,9]
NAV = ' · '.join(f'[{label}](README.md)' if code=='en' else f'[{label}](README_{suffix}.md)' for code,suffix,label in LOCALES)


def neutral(text, code):
    e=read('editorial-copy.json')[code]
    for original, localized in e.get('neutral_replacements',{}).items():
        text=text.replace(original,localized)
    return text.replace('SeaImagine',e['neutral_platform'])


def guide(code,suffix):
    d=read('locale-copy.json')[code]
    c=read('catalog-copy.json')[code]
    parts=[f'# Gemini Omni — {c["guides"]}',f'[{c["index"]}](../../README.md)' if code=='en' else f'[{c["index"]}](../../README_{suffix}.md)']
    if code=='en':
        body=(ROOT/'templates/locales/guide-en.md').read_text()
    else:
        source=json.loads((ROOT/f'templates/locales/README_{suffix}.json').read_text())
        body='\n\n'.join([neutral(source.get('before_examples',''),code),f'## {d["dialogue_title"]}',d['dialogue_note'],f'```text\n{source["dialogue"]}\n```' if source['dialogue'] else '',neutral(source.get('supplemental',''),code)])
    # Existing template links are relative to the repository root.
    body=re.sub(r'\]\((?!https?:|#)([^)]+)\)',lambda m:'](../../'+m[1]+')',body)
    parts += [body,brand_section(code).replace('](assets/','](../../assets/').replace('="assets/','="../../assets/')]
    return '\n\n'.join(parts)+'\n'


def results(code):
    c=read('catalog-copy.json')[code];s=read('community-examples.json')
    rows=['<a id="video-studies"></a>',f'## {c["results"]}',c['result_note'],f'| Google · Omni 1.1 Flash | {c["actions"]} |','|---|---|']
    for i,case in enumerate(s['official']['suggested_cases']):
        rows += [f'| {c["result_titles"][i]} | [{c["watch"]}]({case["url"]}) · [Google]({s["official"]["url"]}) |']
    rows += ['\n| X · Omni / Flash · 2026-05 | X · Omni / Flash · 2026-05 |','|---|---|']
    cards=[]
    for i,case in enumerate(s['community']):
        title=c['result_titles'][i+4];media=case['media'][0]
        card=f'**{title}**<br><a href="{case["url"]}"><img src="{media["thumbnail_url"]}" alt="{title}" width="240"></a><br>{case["author"]}<br>[{c["source_link"]}]({case["url"]}) · [{c["watch"]}]({media["url"]})'
        if case.get('prompt_reply_url'):
            card+=f' · [{c["prompt"]}]({case["prompt_reply_url"]})'
        cards.append(card)
    rows += ['| '+' | '.join(cards[i:i+2])+' |' for i in range(0,len(cards),2)]
    rows += [f'[{c["source_link"]} / FxTwitter](docs/community-examples.md)']
    return '\n\n'.join(rows[:3])+'\n\n'+'\n'.join(rows[3:])


def build(code,suffix):
    d=read('locale-copy.json')[code];e=read('editorial-copy.json')[code];c=read('catalog-copy.json')[code];a=read('homepage-additions.json')[code]
    src=json.loads((ROOT/f'templates/locales/README_{suffix}.json').read_text())
    nav_items=NAV.split(' · ');nav=' · '.join(nav_items[:10])+'\n\n'+' · '.join(nav_items[10:])
    shortcuts=f'[{c["browse"]}](#prompt-collections) · [{c["gallery"]}](#source-examples) · [{c["results"]}](#video-studies) · [{c["index"]}](docs/prompt-index.md) · [{c["download_all"]}](prompts/copy/all-prompts.txt)'
    parts=['<div align="center">',f'![{e["title"]}](assets/seaimagine-omni-hero.png)',f'# {e["title"]}',f'**{c["intro"]}**',nav,shortcuts,'</div>','<a id="prompt-collections"></a>',f'## {c["browse"]}']
    labels=[x[0] for x in src['collections']] if src['collections'] else EN_COLLECTIONS
    table=[f'| {c["category"]} | {c["cases"]} | {c["actions"]} |','|---|---:|---|']
    for i,(path,label) in enumerate(zip(PATHS,labels)):
        # Source translations include counts; avoid repeating them in category names.
        label=re.split(r'[:：]',label)[0]
        table += [f'| [{label}](prompts/{path}.md) | {COUNTS[i]} | [{c["open"]}](prompts/{path}.md#case-01) |']
    parts += ['\n'.join(table),f'[{c["index"]}](docs/prompt-index.md) · [{c["download_all"]}](prompts/copy/all-prompts.txt)',d['language_note'],'<a id="source-examples"></a>',f'## {c["gallery"]}',c['input_note']]
    examples=read('showcase-examples.json')+read('brand-examples.json')
    titles=[d[f'example{i}'] for i in range(1,4)]+a['brand_titles']
    parts += [' · '.join(f'[{i+1:02} · {title}](#example-{i+1:02})' for i,title in enumerate(titles))]
    for i,(ex,title) in enumerate(zip(examples,titles)):
        prompt=ex.get('prompt_en',ex['prompt']) if code=='en' else ex['prompt']
        file=f'prompts/copy/showcase-{i+1:02}'+('-en' if code=='en' and i<3 else '')+'.txt'
        category_i=[1,2,3,1,3,1][i]
        category_label=re.split(r'[:：]',labels[category_i])[0]
        parts += [f'<a id="example-{i+1:02}"></a>',f'### {i+1:02} · {title}',f'<a href="assets/{ex["image"]}"><img src="assets/{ex["image"]}" alt="{title}" width="420"></a>',f'[{category_label}](prompts/{PATHS[category_i]}.md) · [{c["reference"]}](assets/{ex["image"]}) · [{c["copy"]}]({file})',f'```text\n{prompt}\n```']
        if i==5:parts += [a['caption']]
    parts += [results(code),f'## {c["guides"]}',f'{c["guides_note"]} [{c["open"]}](docs/guides/README_{suffix}.md)',f'[{d["prompting"]}](docs/prompting-guide.md) · [{d["multilingual"]}](docs/multilingual-guide.md) · [{d["reference"]}](docs/reference-videos.md)','<a id="brand-tools"></a>',f'## {c["brand"]}']
    base='https://seaimagine.com'+('' if code=='en' else '/'+code)
    parts += [f'[Gemini Omni]({base}/model/gemini-omni/) · [Gemini Omni 1.1 Flash]({base}/model/gemini-omni-1-1-flash/)',f'[{d["i2v"]}]({base}/image-to-video/) · [{d["t2v"]}]({base}/text-to-video/) · [{d["imagegen"]}]({base}/ai-image-generator/)',d['tools_note'],f'[{d["workflow"]}](docs/seaimagine-workflow.md)',f'## {d["source_title"]}',d['source'],'[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE) · [Contributing](CONTRIBUTING.md)']
    return '\n\n'.join(parts)+'\n'


def generate():
    update_workflow()
    (ROOT/'docs/guides').mkdir(exist_ok=True)
    (ROOT/'prompts/copy').mkdir(exist_ok=True)
    for i,ex in enumerate(read('showcase-examples.json')+read('brand-examples.json')):
        (ROOT/f'prompts/copy/showcase-{i+1:02}.txt').write_text(ex['prompt']+'\n')
        if 'prompt_en' in ex:(ROOT/f'prompts/copy/showcase-{i+1:02}-en.txt').write_text(ex['prompt_en']+'\n')
    for code,suffix,_ in LOCALES:
        (ROOT/f'README_{suffix}.md').write_text(build(code,suffix))
        (ROOT/f'docs/guides/README_{suffix}.md').write_text(guide(code,suffix))
    (ROOT/'README.md').write_text((ROOT/'README_EN.md').read_text())
    print('Built 15 catalogue homepages and 15 separate guides.')


if __name__=='__main__':generate()
