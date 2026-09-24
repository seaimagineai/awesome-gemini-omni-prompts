# Reader-first homepage order — 2026-09-24

The user requested official model examples and community examples first, followed by the prompt library and usage, with SeaImagine introduced at the end. This supersedes the previous brand-first homepage order.

All 15 language homepages now follow that sequence. The English mirror remains identical to README.md. Official examples link to Google's announcement; community examples retain author links and now also expose the Google AI quotation and FxTwitter evidence links. Version and evidence limits remain explicit.

The three source examples, three new illustrated exercises, teaching sections and product links are retained. Code-block and image-source multisets were compared against the prior commit for all 16 README files and were identical. Source recipe and teaching validation remains in place. Generation was repeated and was deterministic.

An independent reviewer identified grammatical problems caused by replacing a brand name with a generic tool phrase. The main agent accepted this finding; affected sentences were rewritten in context, with replacements maintained in data/editorial-copy.json. The homepage generator now applies these full-sentence replacements. CONTRIBUTING.md documents the intended order and the new copy file.

The reviewer rechecked the regenerated pages and reported no remaining required fixes. The main agent independently repeated code/image preservation comparisons, deterministic generation and repository validation, then rendered English, Chinese, Japanese and Arabic through GitHub’s Markdown API. All four retained real image and code-block elements in the intended section order. These checks concern documentation and rendering, not model generation or native X playback.
