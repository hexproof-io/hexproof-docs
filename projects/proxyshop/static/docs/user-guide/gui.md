# 💻 Using the Proxyshop GUI

## Render Cards Tab

- The main tab for rendering authentic Magic the Gathering cards.
- **Render All**: Renders a card image using each art image found in the `art/` folder.
- **Render Target**: Opens file select in Photoshop, renders a card image using each art image you select.
- **Global Settings**: Opens a settings panel used to change app-wide options for:
    - **Main settings**: Affects template behavior, can be modified for individual templates. When you click the ⚙️ icon next to a template, a config file is generated for **that** template which overrides these settings.
    - **System settings**: Affects the entire application and cannot be changed for individual templates.
- The set of tabs below these buttons represent **template types**, e.g. Normal, MDFC, Transform, etc.
    - **Template types** represent different kinds of templates which require different frame elements or different rendering techniques.
    - If the **Normal** tab is active, and you click on a template button, that template becomes selected for the **Normal** template type. Cards which match the **Normal** type will now render using that template. 
    - That template **DOES NOT** become selected for other types. For example, if **Borderless** is selected in the **Normal** tab, but **Normal** is selected in the **MDFC** tab. Cards that match the **MDFC** type will render using **Normal MDFC**.
- Next to each template in the template list there are two icons:
    - ⚙️ Lets you change the **Main Settings** for this template, some templates will also have their own specially designed settings you can change as well.
    - 🧹 Deletes the separate config file generated for this template, effectively returning this template back to default settings. Ensures **Main Settings** for this template are governed by the **Global Settings** panel.
- The dark grey area below the templates selector is the **Console**, this is where status messages will be displayed tracking render progress and other user actions.
- To the right of the **Console** are some useful buttons:
    - 📌 Pins the Proxyshop window, so it remains above all other running programs
    - 📷 Takes a screenshot of the Proxyshop window, saves to: `out/screenshots/`
    - 🌍 Opens your default web browser, navigating to Proxyshop's GitHub page
    - ❔ Opens your default web browser, navigating to our community Discord server
    - **Continue**: Becomes active when app is waiting for a user response, either when manual editing is enabled or an error has occurred.
    - **Cancel**: Becomes active when cards are being rendered, can cancel the render operation at any time or if an error occurs.
    - **Update**: Opens the **Updater** panel which allows you to download new templates and update existing ones.

## Custom Creator Tab

- This tab controls the custom card creator.
- This feature is currently considered **experimental beta** and may have issues.
- You can currently render **Normal**, **Planeswalker**, or **Saga** cards, just fill in the appropriate data and hit **Render Custom**.
- More features and card types will be added in the near future.

## Tools Tab

- This tab contains a growing list of helpful tools and utilities.
- **Render All Showcases**: Generates a bordered showcase image for each card image in the `out/` folder, showcases will be placed in `out/showcase/`.
- **Render Target Showcase**: Opens a file select in Photoshop, generates a bordered showcase image for each card image you select.
- **Compress Renders**: This tool reduces the size of card images stored in the `out/` folder. The settings are:
    - **Quality**: JPEG save quality of the compressed image, supports a number between 1 and 100. (**Recommended**: 95-100)
    - **Optimize**: Enables Pillow's automatic "optimize" flag. Lowers filesize by a small margin for no discernible downside. (**Recommended**: On)
    - **800 DPI**: Downscales card images above 800 DPI to a maximum of 800 DPI. Most Proxyshop templates are 1200 DPI which is much higher than anyone really needs. Most printing services do not print above 800 DPI. (**Recommended**: On)
