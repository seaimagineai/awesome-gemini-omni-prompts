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

def update_workflow():
    p=ROOT/'docs/seaimagine-workflow.md';s=p.read_text()
    a=s.index('<!-- generated:practice:start -->')+len('<!-- generated:practice:start -->')
    b=s.index('<!-- generated:practice:end -->',a)
    section=brand_section('en').replace('](assets/','](../assets/').replace('="assets/','="../assets/')
    p.write_text(s[:a]+'\n'+section+'\n'+s[b:])
