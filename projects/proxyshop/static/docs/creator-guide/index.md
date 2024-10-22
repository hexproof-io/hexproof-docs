# Installing for Creators

## 🛠️ Requirements

- Photoshop (Minimum: 2018+, Recommended: 2020+)
- Windows (Not currently compatible with Mac/Linux)
- [The Photoshop templates](https://drive.google.com/drive/u/1/folders/1moEdGmpAJloW4htqhrdWZlleyIop_z1W) (Can be downloaded in the app)
- Required fonts (included in `fonts/`):
    - **Beleren Proxy Bold** — For Card Name, Typeline, Power/Toughness
    - **Proxyglyph** — For mana symbols, a fork of Chilli's NDPMTG font
    - **Plantin MT Pro** — For rules text, install **all** variants included
    - **Beleren Smallcaps** — For Artist credit line and miscellaneous
    - **Gotham Medium** — For collector text
- Optional (but recommended) fonts:
    - **Magic The Gathering** — Required by Classic template
    - **Matrix Bold** — Required by Colorshifted template
    - **Mana** — For various additional card symbols

## 🐍 Setup Guide

Setting up the Python environment for Proxyshop is intended for advanced users, contributors, and anyone who wants to 
get their hands dirty making a plugin or custom template for the app! This guide assumes you already have Python installed.
See the badge above for supported Python versions.
1. Install Poetry with pipx.
    ```bash
    ## Install pipx and poetry
    python -m pip install --user pipx
    python -m pipx ensurepath
    pipx install poetry
    ```
2. Clone Proxyshop somewhere on your system, we'll call this the ***root directory***.
    ```bash
    git clone https://github.com/MrTeferi/Proxyshop.git
    ```
3. Navigate to the **root directory** and install the project environment.
    ```bash
    cd proxyshop
    poetry install
    ```
4. Install the fonts included in the `fonts/` folder. Do not delete these after install, some are used by the GUI. It is 
recommended to install all fonts in this folder, but some are technically optional (see 
[About Fonts](/proxyshop/user-guide/fonts) for more info).
5. Create a folder called `art` in the root directory. This is where you place art images for cards you wish to render.
6. Run the app.
    ```bash
    ## OPTION 1) Execute via poetry
    poetry run main.py
    
    ## OPTION 2) Enter the poetry environment, then execute with cli
    poetry shell
    proxyshop gui
    ```

## Navigating the GUI

See the GUI [usage guide](./user-guide/gui) for navigating the app.