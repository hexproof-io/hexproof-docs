# 🎨 About Art Files

## Supported Filetypes

Proxyshop currently supports art files with the following file types: `jpg`, `jpeg`, `jpf`, `png`, `tif`, and `webp`[^1].
Art files should be named after **real Magic the Gathering cards** and should be named as accurately as possible, e.g. 
`Damnation.jpg`.

## Art File Tags

Proxyshop supports a number of tags that can be used in the art filename to change how data for that card is fetched
from Scryfall and how the card is rendered by Proxyshop.

### `[set]`

:   When fetching card data[^2], Proxyshop will look for the version of this card printed in the given set.

    **Example:** Fetching the card "Damnation" from "Time Spiral Remastered" (TSR).

    ```
    Damnation [TSR].jpg
    ```

### `{number}`

:   When fetching card data, Proxyshop will look for the version of this card with the provided collector number. This
    is best used in conjunction with `[set]`. When using both, Scryfall will return an _exact_ match for a specific 
    printing of this card.

    **Example:** Fetching the non-promo version of "Damnation" from "Time Spiral Remastered" (TSR), which is #106.

    ```
    Damnation [TSR] {106}.jpg
    ```

### `(Artist Name)`

:   When rendering this card, Proxyshop will replace the arist name present in Scryfall data with the name provided.

    **Example:** Rendering the card "Damnation" with the artist name "Rusty Shackleford".

    ```
    Damnation (Rusty Shackleford).jpg
    ```

### `$Creator`

:   When rendering this card, Proxyshop will fill in your "Creator" name in the appropriate text layer if the Photoshop 
    template supports it. This is not the same as "Artist Name" and not all templates support it. This is meant to be 
    the name of the person who rendered the card, not the artist who created the card's art.

    **Example:** Rendering the card "Damnation" with the creator name "Investigamer", note that this tag **MUST** be 
    placed at the very end of the filename, otherwise the "Creator" field might capture unintended characters.

    ```
    Damnation [TSR] {106} (Rusty Shackleford) $Investigamer.jpg
    ```

[^1]: WEBP files are only supported by Photoshop 2022 and above.
[^2]: Proxyshop pulls card data primarily from the Scryfall API. Tags that relate to fetching specific card data
from Scryfall do not apply to custom generated cards where the user provides the data.