# Installing the App

This documentation is for installing and using the official Proxyshop executable release. If you plan to get your hands 
dirty with developing plugins, custom templates, or modifying Proxyshop's source code, please follow the 
[Creator Guide](../creator-guide) to set up Proxyshop's Python project environment.

## 🛠️ Requirements

- Photoshop (**Minimum:** 2018+, **Recommended:** 2022+)
- Windows (Not currently compatible with Mac/Linux)
- Python 3.10+ (**Recommended**: 3.12)
- An internet connection

## 🚀 Setup Guide

1. Download the [latest release](https://github.com/MrTeferi/MTG-Proxyshop/releases), extract it to a folder of your choice.
2. Install the fonts included in the `fonts/` folder. It is recommended to install all fonts in this folder, but some 
are technically optional (see [About Fonts](../user-guide/fonts) for more info). If updating from a previous 
Proxyshop version, make sure to check the release notes to see if any fonts need to be updated.
3. Place card arts for cards you wish to render in the `art/` folder. These arts should be named according to the card 
(see [About Art Files](../user-guide/art) for more info).
4. Launch `Proxyshop.exe`. Click the **Update** button. Proxyshop will load templates available to download, grab what you want.
5. Hit **Render All** to render every card art in the `art/` folder. Hit **Render Target** to render one or more specific card arts.
6. You can also drag art images or folders containing art images onto the Proxyshop app, Proxyshop will automatically start rendering those cards.
7. During the render process the console at the bottom will display the current progress and prompt you if any failures occur.

