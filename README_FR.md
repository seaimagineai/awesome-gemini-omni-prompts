# Prompts vidéo Gemini Omni pour SeaImagine

[English](README.md) · [简体中文](README_ZH.md) · [繁體中文](README_ZH-TW.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md) · [Français](README_FR.md) · [Deutsch](README_DE.md) · [Português](README_PT.md) · [Italiano](README_IT.md) · [Русский](README_RU.md) · [Bahasa Indonesia](README_ID.md) · [ไทย](README_TH.md) · [Tiếng Việt](README_VI.md) · [العربية](README_AR.md)

![Prompts vidéo Gemini Omni pour SeaImagine](assets/seaimagine-omni-hero.png)

Cette bibliothèque conserve les 60 recettes de Flaq AI et ajoute trois exercices SeaImagine avec des images originales. Retrouvez ici ces exercices, les exemples du dépôt source et les enseignements des cas officiels et communautaires.

[Gemini Omni](https://seaimagine.com/fr/model/gemini-omni/) · [Gemini Omni 1.1 Flash](https://seaimagine.com/fr/model/gemini-omni-1-1-flash/)

[Trois exercices SeaImagine avec des images originales](#sea-practice) · [Trois prompts à copier](#source-examples) · [Ce qu’enseignent les exemples officiels et communautaires](#video-studies)

## Premiers pas avec SeaImagine

1. Ouvrez la page du modèle et vérifiez l’accès, le prix et les réglages disponibles.
2. Pour conserver l’apparence d’un produit ou d’un personnage, choisissez image vers vidéo, importez une image et collez le prompt associé. Pour inventer une scène, essayez texte vers vidéo.
3. Réglez la durée et le format dans l’interface. Testez un plan, vérifiez l’apparence, le mouvement et le son, puis modifiez une seule consigne à la fois.

Ce sont des propositions de prompts, pas des résultats de génération vérifiés sur SeaImagine. Durée, son, montage, prolongement et références dépendent du modèle et de l’interface actuelle. Les fonctions de l’API Google ne sont pas automatiquement disponibles sur SeaImagine.

<a id="sea-practice"></a>

## Trois exercices SeaImagine avec des images originales

Ces images de référence ont été générées par IA pour servir de première image aux exercices. Ce ne sont pas des résultats vidéo testés avec Gemini. Utilisez les fonctions présentes dans votre interface SeaImagine.

### SEA-01 · Une tasse en céramique bleu-vert au petit matin

[![Une tasse en céramique bleu-vert au petit matin](assets/seaimagine-ceramic-cup.png)](assets/seaimagine-ceramic-cup.png)

Approchez lentement la caméra sans modifier l’anse, le bord ni le niveau du liquide. Gardez de la place pour le texte final.

Importez l’image de la tasse pour l’animer. Essayez un simple rapprochement lent et vérifiez l’anse et le liquide avant d’ajouter le texte.

[Image vers vidéo](https://seaimagine.com/fr/image-to-video/) · [Générateur d’images IA](https://seaimagine.com/fr/ai-image-generator/)

```text
Use the uploaded ceramic-cup image as the exact first frame. Create a 10-second, 16:9 product shot.
Preserve the teal glaze, the single handle on the right, the rim shape, the coffee level and the cup's position on the wooden table.
[0-3s] A thin ribbon of steam rises; the camera begins a very slow forward move.
[3-7s] Warm morning light grazes the glaze. Keep the table and background still; only steam and gentle reflections move.
[7-10s] The camera eases to a stop. Hold the same product with clean space above for a caption added later.
Audio, if supported: quiet room ambience and one distant bird. No speech or music.
No pouring, added cup, new handle, object morphing, generated text, logo or watermark.
```

### SEA-02 · Un port en papier qui s’illumine

[![Un port en papier qui s’illumine](assets/seaimagine-paper-harbor.png)](assets/seaimagine-paper-harbor.png)

Dans un seul plan, allumez le phare puis augmentez à tour de rôle la lumière aux fenêtres des trois maisons. Conservez la texture du papier et la géométrie.

Importez le port et demandez l’allumage du phare, puis l’intensification successive des lumières aux fenêtres. Comparez la forme des bâtiments au début et à la fin.

[Image vers vidéo](https://seaimagine.com/fr/image-to-video/) · [Générateur d’images IA](https://seaimagine.com/fr/ai-image-generator/)

```text
Use the uploaded paper-harbor image as the exact first frame. Animate a single 10-second, 16:9 shot while retaining the handcrafted paper texture, folds and miniature scale.
Keep the ivory lighthouse with its red roof, the three small houses on the left and the single paper boat in exactly the same positions.
[0-3s] The lighthouse window slowly glows warm amber. The camera begins a small, straight forward move.
[3-7s] The already warm house windows brighten gently one house at a time, from nearest to farthest. No building moves or changes shape.
[7-10s] The camera stops. Hold the warm windows against the blue-hour paper harbor. Keep the boat and miniature water surface still.
Audio, if supported: a quiet original celesta phrase, no voices.
No ocean waves, added buildings, extra boats, rotating tower, camera cut, text, logo or watermark.
```

### SEA-03 · Une pochette en lin pour une boutique multilingue

<a href="assets/seaimagine-linen-pouch.png"><img src="assets/seaimagine-linen-pouch.png" alt="Une pochette en lin pour une boutique multilingue" width="360"></a>

Créez une vidéo verticale sans texte, puis ajoutez les sous-titres traduits dans un logiciel de montage classique.

Animez la pochette au format vertical et ajoutez les traductions ensuite. N’utilisez une courte consigne de retouche vidéo que si cette fonction est disponible.

[Image vers vidéo](https://seaimagine.com/fr/image-to-video/) · [Générateur d’images IA](https://seaimagine.com/fr/ai-image-generator/)

```text
Use the uploaded linen-pouch photograph as the exact first frame. Create a 10-second, 9:16 vertical ecommerce product shot.
Keep one natural-linen drawstring pouch upright in the same position. Preserve its seam placement, woven texture, silhouette and teal drawstring.
[0-3s] Start on the supplied framing. The camera slowly moves forward without orbiting.
[3-7s] A soft highlight travels gently across the fabric; the pouch and its string do not move.
[7-10s] Stop the camera and hold the product. Keep the lower quarter of the frame empty, evenly lit and free of objects for a caption added in editing.
Audio, if supported: soft room tone. No speech or music.
Do not generate any lettering, subtitles, symbols, price, logo, watermark, extra bag or moving string.
```

> Le quotidien, tout simplement

<a id="source-examples"></a>

## Trois prompts à copier

Ces images sont des premières images de référence reprises du dépôt source, pas des résultats vidéo. Importez l’image correspondante comme Image1. Les 10 secondes et le son indiquent le résultat souhaité ; adaptez-les aux réglages disponibles.

### 01 · Enceinte : rythme des gouttes

![Enceinte : rythme des gouttes](assets/product-speaker.png)

```text
Create a 10-second premium product film from Image1. Use Image1 as the exact starting frame.

[0-3s] Make a slow 20-degree clockwise camera orbit. Suspended droplets travel around the speaker in clean concentric paths, aligned to a deep electronic kick. Preserve the speaker's exact coral color, grille weave and proportions.
[3-7s] A sunrise reflection sweeps across the copper end cap. On the snare, droplets strike the wet stone and rebound as fine mist.
[7-10s] All droplets collapse into one crisp splash behind the product, then settle on a steady three-quarter hero frame with negative space on the right.

Audio: original minimal electronic rhythm at 96 BPM, water-drop percussion, distant ocean ambience. No vocals.
No product morphing, added controls, text, logo, watermark, hands, duplicate product or camera shake.
```

### 02 · Cyclisme sur une crête : ouverture documentaire

![Cyclisme sur une crête : ouverture documentaire](assets/travel-cyclist.png)

```text
Animate Image1 as a single continuous 10-second documentary tracking shot. Use it as the exact first frame.

The cyclist pedals steadily toward the observatory while the camera follows from the same height. Silver grass bends in two wind gusts, loose gravel reacts under the rear tire, and clouds move slowly below the ridge. At 6s, the first warm sunlight reaches the jacket and observatory dome.

Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.
No cuts, drone rise, extra cyclists, landmark text, logo or watermark.
```

### 03 · Horloger et oiseaux de papier : récit illustré

![Horloger et oiseaux de papier : récit illustré](assets/clockmaker-story.png)

```text
Bring this illustration to life in one coherent 10-second animated shot. Use Image1 as the first frame and preserve its watercolor-and-ink direction.

[0-3s] The brass door clicks open and warm light grows inside it. Nearby gears rotate at different believable speeds.
[3-7s] Paper birds unfold one by one and spiral past the camera with visible paper flex. Tilt upward to follow them through the clock opening.
[7-10s] The flock crosses the moon; one tiny paper bird lands on the clock hand.

Audio: layered clock ticks, delicate paper folds, wooden gear creaks, then an original celesta motif. No dialogue.
Keep the clockmaker's face, clothes and goggles consistent. No photorealism, subtitles, logo or watermark.
```



<a id="video-studies"></a>

## Ce qu’enseignent les exemples officiels et communautaires

Les vidéos de Google présentent Omni 1.1 Flash, pas des résultats SeaImagine. Les publications communautaires datent de mai 2026 et concernent la première version d’Omni / Flash ; elles ne constituent pas des tests confirmés de la version 1.1. Les éléments consultés sont le texte et les métadonnées de FxTwitter, sans vérification de la lecture native sur X. Vérifiez les fonctions dans SeaImagine.

### Google : transition entre deux images clés

[Voir l’exemple original](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/sm_KW_omni-flash__capability-video__first-last-frame__16x9_1.mp4)

Définissez séparément l’image de départ, celle d’arrivée et le mouvement continu qui les relie.

Prenez deux photos du même objet sous des angles compatibles. Si les images de début et de fin sont acceptées, reliez-les par un mouvement simple.

### Google : prolonger un plan

[Voir l’exemple original](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/omni-flash__capability-video__extend-multi-cinematography__16x9_25YzzFv.mp4)

Décrivez le mouvement de caméra suivant tout en conservant le sujet et sa direction.

Utilisez votre propre clip. Si la prolongation est disponible, ajoutez une seule suite et recherchez les ruptures de mouvement ou d’éclairage au raccord.

### CHRIS FIRST : transformer les personnes en flamants roses

<a href="https://x.com/chrisfirst/status/2056797606509158681"><img src="https://pbs.twimg.com/amplify_video_thumb/2056797343085969408/img/o5L2FQvozlZtiFsK.jpg" alt="CHRIS FIRST : transformer les personnes en flamants roses" width="300"></a>

[Voir l’exemple original](https://x.com/chrisfirst/status/2056797606509158681)

Remplacez le sujet en demandant de conserver ses vêtements et son action ; vérifiez les points de contact des membres.

Si la retouche vidéo est disponible, remplacez un seul sujet dans votre clip. Comparez les vêtements, la posture et le contact avec le sol.

### Justine Moore : changer de chapeau à chaque claquement de mains

<a href="https://x.com/venturetwins/status/2056793856843366789"><img src="https://pbs.twimg.com/amplify_video_thumb/2056793760273686528/img/tZQnlGWzgr5wOwnM.jpg" alt="Justine Moore : changer de chapeau à chaque claquement de mains" width="300"></a>

[Voir l’exemple original](https://x.com/venturetwins/status/2056793856843366789)

Utilisez un geste visible pour déclencher chaque changement, sans modifier le visage, la tenue ni la caméra.

Filmez deux claquements de mains nets avec une caméra fixe. Si la retouche vidéo est disponible, demandez un changement de chapeau à chaque geste et vérifiez le moment image par image.

[Exemples officiels et communautaires](docs/community-examples.md)

## Contenu

Cette liste décrit des éléments à prévoir dans les prompts, sans garantir leur disponibilité. Vérifiez les entrées, le montage, la prolongation, le son et la résolution dans le modèle choisi sur SeaImagine. Testez d’abord la composition, les paroles et le texte avec un aperçu disponible. L’API de Google (interface de programmation) et l’interface SeaImagine sont distinctes.

- Texte-vers-vidéo, image-vers-vidéo, première/dernière image et références de sujets.
- Conception conjointe de l’image, des ambiances, du bruitage, de la musique originale, du silence et du dialogue.
- Règles de dialogue et de texte à l’écran pour 15 langues.

## Les 60 prompts

Les cinq premières collections sont expliquées en chinois et les deux dernières en anglais. Tous les prompts à copier sont en anglais. Les collections ne sont pas intégralement traduites.

- [Cinéma et narration : 8 prompts](prompts/cinematic-storytelling.md)
- [Commerce et réseaux sociaux : 8 prompts](prompts/commerce-social.md)
- [Documentaire, voyage et éducation : 8 prompts](prompts/documentary-education.md)
- [Animation, musique et divertissement : 8 prompts](prompts/stylized-entertainment.md)
- [Contrôle, édition et extension : 10 recettes](prompts/control-editing-extension.md)
- [Montage avancé, caméra et transformation visuelle : 9 prompts](prompts/advanced-editing-camera.md)
- [Storyboards, écrans partagés, texte et évaluation : 9 prompts](prompts/storyboard-text-evaluation.md)

## Dialogues en français

Vous pouvez conserver les consignes de mise en scène en anglais et préciser mot pour mot le dialogue et le texte visible en français. Vérifiez prononciation, orthographe et synchronisation.

```text
Spoken language: French.
Exact dialogue at 6s, spoken once with natural conversational pacing: "Aujourd'hui, prenons le chemin le plus long pour rentrer."
Do not translate, paraphrase, repeat or subtitle it.

Exact on-screen French title: "PETITS VOYAGES"
Preserve accents, apostrophes and spelling exactly. No other text.
```

## Pour aller plus loin

- [Parcours SeaImagine](docs/seaimagine-workflow.md)
- [Exemples officiels et communautaires](docs/community-examples.md)
- [Guide multilingue](docs/multilingual-guide.md)
- [Conception des prompts](docs/prompting-guide.md)
- [Références et autorisations](docs/reference-videos.md)

## Autres outils SeaImagine

Ces pages offrent d’autres points de départ. Consultez chaque page pour connaître les modèles, conditions et tarifs actuels. Ce dépôt ne garantit pas une disponibilité continue.

- [Créer](https://seaimagine.com/fr/create/)
- [Image vers vidéo](https://seaimagine.com/fr/image-to-video/)
- [Texte vers vidéo](https://seaimagine.com/fr/text-to-video/)
- [Générateur d’images IA](https://seaimagine.com/fr/ai-image-generator/)

## Source et licence

Adaptation du dépôt Flaq AI, dont les collections de prompts et trois images sont reprises. Tout ce contenu n’est pas une création originale de SeaImagine. Guide indépendant, non officiel Google.

[Flaq AI · awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) · [MIT](LICENSE)
