# :fontawesome-solid-pen-nib: About Fonts

Each Proxyshop release (and the source repository) contains a `/fonts` directory containing all fonts used by 
the app. Generally, it is recommended to install all fonts in this folder, but strictly speaking some are **optional**.
Here we document the fonts which are required and optional, what they are used for, and the credited source of these 
fonts.

All fonts provided with the app are re-published for **NON-COMMERCIAL USE, FOR UNOFFICIAL FAN CONTENT**. We provide 
no guarantees, warranties, or other support for these fonts and accept no liability nor responsibility for their use.

## Required Fonts

### Beleren Proxy Bold

:   Used for Card Name, Typeline, and/or Power/Toughness text on a variety of templates.

    **Source:** This font is owned by Wizards of the Coast and was originally extracted from 
    [their official website](https://magicthegathering.com) by another party. The font has been modified 
    to include some missing characters required by some cards and is published for non-commercial use 
    for unofficial fan content ONLY.

### Proxyglyph

:   Used for Mana Cost symbols and other symbols.

    **Source:** This font is largely based on Chilli's original NDPMTG font. We've made some adjustments and added 
    support for new symbols that were previously missing. This is largely a fork of Chilli's font that is maintained 
    separately.

### Plantin MT Pro

:   Used primarily for rules text. Make sure to install all included variants of this font (regular, bold, italic, 
    etc). Theoretically, you can skip the `SemiBdIt` version if you never plan to render "Nickname" cards.

    **Source:** The Plantin MT Pro font family was designed by Frank Hinman Pierpont for Monotype and is free 
    for personal use. The original Plantin font family was designed by Robert Granjon and Frank Hinman Pierpont 
    for Monotype, but is no longer used by this project.

### Beleren Small Caps

:   Used for Artist name and other miscellaneous cases.

    **Source:** This font is owned by **Wizards of the Coast**, it is not clear whether this font was extracted as a 
    site resource or recreated by a freelance designer. Please reach out to me if you have more details.

### Gotham Medium

:   Used for collector info text and other miscellaneous cases.

    **Source:** The Gotham Medium font family was designed by Hoefler Type Foundry Inc and is free for personal use.

## Optional Fonts

### Magic the Gathering

:   Required for the Classic template (and most other Classic-based templates).

    **Source:** Created by Mike Hind, likely owned by Wizards of the Coast, listed as free for personal use. This 
    font is largely similar to "Goudy Medieval".

### Matrix Bold

:   Required for the Colorshifted template.

    **Source:** The Matrix II font family designed by Zuxana Licko, licensed and distributed by Emigre. Through the 
    Adobe Fonts library this font family is cleared for both personal and commercial use.

### Mana

:   Primarily used for icons in Transform templates. If you plan to render any Transform cards you should almost 
    certainly install this font.

    **Source:** Developed and maintained by [Andrew Gioia](https://github.com/andrewgioia), distributed via his 
    [website](https://mana.andrewgioia.com) for personal use. The symbols themselves are trademarks owned by 
    Wizards of the Coast.

## Deprecated Fonts

These are fonts which were used by Proxyshop in the past but have since been deprecated and are no longer used
by the official Proxyshop project.

### Keyrune

:   Proxyshop used to generate expansion symbols using Andrew Gioia's [Keyrune](https://keyrune.andrewgioia.com/) font, 
    but now we exclusively used SVG files from the [`mtg-vectors`](/mtg-vectors/) catalog. Symbols used in this font are
    trademarks owned by Wizards of the Coast. Some symbols in the `mtg-vectors` catalog were designed using a symbol 
    provided by one of Andrew's repositories as source material, so his work continues to be invaluable to this day.
