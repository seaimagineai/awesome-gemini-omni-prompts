"""Shared on-page practice sections; English control prompts, localized explanations."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT/'data'/name).read_text())

def brand_section(code):
    a=read('homepage-additions.json')[code]
    d=read('locale-copy.json')[code]
    prefix='' if code=='en' else '/'+code
    rows=['<a id="sea-practice"></a>',f'## {a["brand_heading"]}',a['brand_note']]
    for i,e in enumerate(read('brand-examples.json')):
        rows += [f'### {e["id"]} · {a["brand_titles"][i]}',
                 (f'<a href="assets/{e["image"]}"><img src="assets/{e["image"]}" alt="{a["brand_titles"][i]}" width="360"></a>' if i==2 else f'[![{a["brand_titles"][i]}](assets/{e["image"]})](assets/{e["image"]})'),
                 a['brand_lessons'][i],a['brand_actions'][i],
                 f'[{d["i2v"]}](https://seaimagine.com{prefix}/image-to-video/) · [{d["imagegen"]}](https://seaimagine.com{prefix}/ai-image-generator/)',
                 f'```text\n{e["prompt"]}\n```']
        if i==2:
            # This specifies post-production text, not a claimed editor/API feature.
            rows += [f'> {a["caption"]}']
    return '\n\n'.join(rows)

def studies_section(code):
    a=read('homepage-additions.json')[code]
    s=read('community-examples.json')
    official=s['official']['suggested_cases']
    studies=[(official[1]['url'],None,s['official']['url']),
             (official[0]['url'],None,s['official']['url']),
             (s['community'][0]['url'],s['community'][0]['media'][0]['thumbnail_url'],s['community'][0]['evidence_url']),
             (s['community'][1]['url'],s['community'][1]['media'][0]['thumbnail_url'],s['community'][1]['evidence_url'])]
    rows=['<a id="video-studies"></a>',f'## {a["study_heading"]}',read('editorial-copy.json')[code]['study_note']]
    for i,(url,thumb,evidence) in enumerate(studies):
        rows += [f'### {a["study_titles"][i]}']
        if thumb:
            rows += [f'<a href="{url}"><img src="{thumb}" alt="{a["study_titles"][i]}" width="300"></a>']
        citation = f'[Google]({evidence})' if i<2 else f'[FxTwitter]({evidence}) · [Google AI]({s["community"][i-2]["official_quote_url"]})'
        rows += [f'[{a["watch_label"]}]({url}) · {citation}',a['study_lessons'][i],a['study_practice'][i]]
    d=read('locale-copy.json')[code]
    rows += [f'[{d["community"]}](docs/community-examples.md)']
    return '\n\n'.join(rows)

def library_intro(code):
    e=read('editorial-copy.json')[code]
    return '\n\n'.join([f'## {e["library_heading"]}',e['library_intro'],f'### {e["usage_heading"]}', '\n'.join(f'{i}. {v}' for i,v in enumerate(e['usage_steps'],1))])

def update_english():
    p=ROOT/'README.md';s=p.read_text()
    for label,content in [('brand',brand_section('en')),('studies',studies_section('en')),('library',library_intro('en'))]:
        start=f'<!-- generated:{label}:start -->';end=f'<!-- generated:{label}:end -->'
        a=s.index(start)+len(start);b=s.index(end,a)
        s=s[:a]+'\n'+content+'\n'+s[b:]
    p.write_text(s)
    p=ROOT/'docs/seaimagine-workflow.md';s=p.read_text()
    a=s.index('<!-- generated:practice:start -->')+len('<!-- generated:practice:start -->')
    b=s.index('<!-- generated:practice:end -->',a)
    section=brand_section('en').replace('](assets/','](../assets/').replace('="assets/','="../assets/')
    p.write_text(s[:a]+'\n'+section+'\n'+s[b:])
