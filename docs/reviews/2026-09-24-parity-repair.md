# Source-parity repair — 2026-09-24

This follow-up corrects gaps missed by the [first-release review](2026-09-24.md). The user authorized all four findings from the subsequent source comparison.

## Changes and evidence

| Finding | Repair | Verification |
|---|---|---|
| Source teaching was lost during localization | Restored Chinese need-based navigation, capability planning, limitations, official sources and contribution paths; Japanese/Spanish ten-second templates and text-only edits; Traditional Chinese script constraints; other retained language teaching notes | Source teaching-block fingerprints checked against each generated page, in addition to the unchanged 77 collection code blocks |
| Brand adaptation was concentrated in a cover and linked guide | Added three new first-frame illustrations, full practice prompts and localized instructions to every homepage; retained all three source examples | Main agent and reviewer inspected the actual images; video prompts match the cup, lit house windows and pouch caption space |
| New studies were mostly English links | Added local explanations and concrete practice steps for two official 1.1 Flash studies and two earlier Omni/Flash community studies to all 15 homepages | Original links, author names, mirror evidence limits and version distinction retained; the six-case evidence guide remains accessible |
| English instructions implied a fixed 360p workflow | Changed FAQ to the lowest suitable resolution available in the selected interface; retained 360p only as Google API context | Checked rendered text and absence of the old unconditional instruction |

## Review loop

The independent reviewer checked actual teaching text and image/prompt agreement, not only language-file counts. The first pass found one remaining issue: the English inventory still counted only the three inherited practice images. The main agent accepted the finding and changed it to six images, explicitly split between three new SeaImagine inputs and three inherited inputs.

The generated brand/practice sections are owned by `scripts/homepage_sections.py`; localized explanations are in `data/homepage-additions.json`. The restored source templates remain in `templates/locales/`. Generation is deterministic and was run twice with unchanged byte hashes. The three generated images have complete production briefs and hashes in `data/brand-asset-provenance.json`.

These changes do not establish native X playback, paid generation success, model output quality, or long-term product availability. New images are practice inputs, not Gemini-generated video results. The previous review's unconditional completion statement is superseded by this broader source-parity check.

## Final review and independent check

The reviewer rechecked the six-image inventory and the final regenerated language pages and reported no remaining P1/P2 findings within these four repair areas. The main agent then independently compared all 77 source collection code blocks; checked six illustrated practice sections and direct study links on every locale page; scanned published Markdown and data for private paths; and rendered English, Chinese, Japanese and Arabic via GitHub's Markdown API. All images and code blocks remained real rendered elements rather than escaped markup. Local validation passed with 779 relative file links, and the generator was idempotent.
