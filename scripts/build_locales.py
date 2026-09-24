#!/usr/bin/env python3
"""Build a browsable prompt catalogue for experienced users in all 15 locales."""
import json
import re
from html import escape
from pathlib import Path
from homepage_sections import brand_section, read, update_workflow

ROOT = Path(__file__).resolve().parents[1]
LOCALES = [('en','EN','English'),('cn','ZH','简体中文'),('tw','ZH-TW','繁體中文'),('ja','JA','日本語'),('ko','KO','한국어'),('es','ES','Español'),('fr','FR','Français'),('de','DE','Deutsch'),('pt','PT','Português'),('it','IT','Italiano'),('ru','RU','Русский'),('id','ID','Bahasa Indonesia'),('th','TH','ไทย'),('vi','VI','Tiếng Việt'),('ar','AR','العربية')]
CATEGORY_DATA = read('category-grid.json')
PATHS = [x['id'] for x in CATEGORY_DATA]
NAV = ' · '.join(f'[{label}](README.md)' if code=='en' else f'[{label}](README_{suffix}.md)' for code,suffix,label in LOCALES)


def featured_examples():
    return read('showcase-v2.json') + read('showcase-v3-additions.json')


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
        body+='\n\n## Earlier source examples\n\n'+'\n\n'.join(f'![Source reference](assets/{case["image"]})\n\n```text\n{case["prompt_en"]}\n```' for case in read('showcase-examples.json'))
    else:
        source=json.loads((ROOT/f'templates/locales/README_{suffix}.json').read_text())
        body='\n\n'.join([neutral(source.get('before_examples',''),code),f'## {d["dialogue_title"]}',d['dialogue_note'],f'```text\n{source["dialogue"]}\n```' if source['dialogue'] else '',neutral(source.get('supplemental',''),code)])
    # Existing template links are relative to the repository root.
    body=re.sub(r'\]\((?!https?:|#)([^)]+)\)',lambda m:'](../../'+m[1]+')',body)
    parts += [body,brand_section(code).replace('](assets/','](../../assets/').replace('="assets/','="../../assets/')]
    return '\n\n'.join(parts)+'\n'


def results(code):
    c=read('catalog-copy.json')[code];v=read('gallery-v2-copy.json')[code]
    cases=read('public-prompt-results.json')['cases']
    parts=['<a id="video-studies"></a>',f'## {c["results"]}',v['results_note']]
    cells=[]
    for i,case in enumerate(cases):
        thumb=case['thumbnail_url'] or ('assets/official-bubbles-link.svg' if i==0 else 'assets/official-recursive-link.svg')
        preview=v['official_video'] if not case['thumbnail_url'] else v['result_titles'][i]
        mode=v[case['mode']]
        cells.append(f'<td width="50%" valign="top"><strong>{escape(v["result_titles"][i])}</strong><br><a href="{case["video_url"]}"><img src="{thumb}" alt="{escape(preview)}" width="100%"></a><br>{escape(case["author"])} · Omni / Flash · 2026-05<br>{escape(mode)}<br><strong>{escape(v["prompt_excerpt"])}</strong><blockquote>{escape(case["prompt_excerpt"])}</blockquote><a href="{case["prompt_url"]}">{escape(v["full_prompt"])}</a> · <a href="{case["video_url"]}">{escape(c["watch"])}</a> · <a href="{case["source_url"]}">{escape(c["source_link"])}</a></td>')
    parts += ['<table width="100%">\n'+'\n'.join('<tr>\n'+'\n'.join(cells[i:i+2])+'\n</tr>' for i in range(0,len(cells),2))+'\n</table>',f'[{c["source_link"]} / FxTwitter](docs/public-prompt-sources.md)']
    return '\n\n'.join(parts)


def build(code,suffix):
    d=read('locale-copy.json')[code];e=read('editorial-copy.json')[code];c=read('catalog-copy.json')[code];v=read('gallery-v2-copy.json')[code]
    catalog=read('prompt-catalog.json');total=len(catalog['cases'])
    index_label=c['index'].replace('60',str(total));labels=v['category_titles']
    nav_items=NAV.split(' · ');nav=' · '.join(nav_items[:10])+'\n\n'+' · '.join(nav_items[10:])
    shortcuts=f'[{c["browse"]}](#prompt-collections) · [{c["gallery"]}](#source-examples) · [{c["results"]}](#video-studies) · [{index_label}](docs/prompt-index.md) · [{c["download_all"]}](prompts/copy/all-prompts.txt)'
    parts=['<div align="center">',f'![{e["title"]}](assets/seaimagine-omni-hero.png)',f'# {e["title"]}',f'**{v["intro"]}**',nav,shortcuts,'</div>','<a id="prompt-collections"></a>',f'## {c["browse"]}']
    counts={x['id']:x['count'] for x in catalog['categories']}
    cells=[]
    for i,category in enumerate(CATEGORY_DATA):
        path=f'prompts/{category["id"]}.md'
        cells.append(f'<td width="33%" align="center" valign="top"><strong><a href="{path}">{escape(labels[i])}</a></strong><br><br><a href="{path}"><img src="{category["image"]}" alt="{escape(labels[i])}" width="100%"></a><br>{counts[category["id"]]} {escape(v["count_label"])}<br><a href="{path}#case-index">{escape(c["open"])}</a></td>')
    parts += ['<table width="100%">\n'+'\n'.join('<tr>\n'+'\n'.join(cells[i:i+3])+'\n</tr>' for i in range(0,9,3))+'\n</table>',v['preview_note'],f'[{index_label}](docs/prompt-index.md) · [{c["download_all"]}](prompts/copy/all-prompts.txt) · [{v["new_sources"]}](docs/public-prompt-sources.md#category-inspiration)',v['language_note'],'<a id="source-examples"></a>',f'## {c["gallery"]}',c['input_note']]
    examples=featured_examples();titles=v['showcase_titles']
    assert len(examples)==len(titles)==9
    parts += [' · '.join(f'[{i+1:02} · {title}](#example-{i+1:02})' for i,title in enumerate(titles))]
    for i,(ex,title) in enumerate(zip(examples,titles)):
        file=f'prompts/copy/{Path(ex["image"]).stem}.txt';category_i=PATHS.index(ex['category'])
        parts += [f'<a id="example-{i+1:02}"></a>',f'### {i+1:02} · {title}',f'[![{title}]({ex["image"]})]({ex["image"]})',f'[{labels[category_i]}](prompts/{ex["category"]}.md) · [{c["reference"]}]({ex["image"]}) · [{c["copy"]}]({file})',f'```text\n{ex["prompt"]}\n```']
    parts += [results(code),f'## {c["guides"]}',v['tutorial_intro'],'\n'.join(f'{i}. {step}' for i,step in enumerate(v['tutorial_steps'],1)),v['tutorial_example_label'],'```text\nChange only the camera movement to a locked-off shot.\nKeep the subject, material, action timing, lighting and audio unchanged.\nDo not add objects, cuts or text.\n```',f'[{c["guides"]}](docs/guides/README_{suffix}.md)',f'[{d["prompting"]}](docs/prompting-guide.md) · [{d["multilingual"]}](docs/multilingual-guide.md) · [{d["reference"]}](docs/reference-videos.md)','<a id="brand-tools"></a>',f'## {c["brand"]}']
    base='https://seaimagine.com'+('' if code=='en' else '/'+code)
    parts += [f'<a href="{base}/"><img src="assets/seaimagine-logo.png" alt="SeaImagine" width="48"></a>',f'[![{c["brand"]}](assets/seaimagine-creative-world.png)]({base}/image-to-video/)',v['brand_intro'],v['brand_bridge']]
    parts += ['\n'.join(f'{i}. {step}' for i,step in enumerate(v['brand_steps'],1)),f'[Gemini Omni 1.1 Flash]({base}/model/gemini-omni-1-1-flash/) · [Gemini Omni]({base}/model/gemini-omni/)',f'[{d["i2v"]}]({base}/image-to-video/) · [{d["t2v"]}]({base}/text-to-video/) · [{d["imagegen"]}]({base}/ai-image-generator/)',f'[{d["workflow"]}](docs/seaimagine-workflow.md)',f'## {d["source_title"]}',d['source'],'[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE) · [Contributing](CONTRIBUTING.md)']
    return '\n\n'.join(parts)+'\n'


def generate():
    update_workflow()
    (ROOT/'docs/guides').mkdir(exist_ok=True)
    (ROOT/'prompts/copy').mkdir(exist_ok=True)
    for ex in featured_examples():
        (ROOT/f'prompts/copy/{Path(ex["image"]).stem}.txt').write_text(ex['prompt']+'\n')
    for i,ex in enumerate(read('showcase-examples.json')+read('brand-examples.json')):
        (ROOT/f'prompts/copy/showcase-{i+1:02}.txt').write_text(ex['prompt']+'\n')
        if 'prompt_en' in ex:(ROOT/f'prompts/copy/showcase-{i+1:02}-en.txt').write_text(ex['prompt_en']+'\n')
    for code,suffix,_ in LOCALES:
        (ROOT/f'README_{suffix}.md').write_text(build(code,suffix))
        (ROOT/f'docs/guides/README_{suffix}.md').write_text(guide(code,suffix))
    (ROOT/'README.md').write_text((ROOT/'README_EN.md').read_text())
    print('Built 15 catalogue homepages and 15 separate guides.')


if __name__=='__main__':generate()
