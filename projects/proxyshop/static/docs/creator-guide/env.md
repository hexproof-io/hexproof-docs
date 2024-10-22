# Environment Variables

Proxyshop supports a handful of environment variables that govern application behavior and are typically only 
useful when developing plugins or contributing to the codebase. To change environment variables, make a copy of
the `/src/data/env.default.yml` file within the same directory and rename the copy to `env.yml`. Then you can
make any changes you feel are necessary. These settings can also be set as environment variables in the OS 
environment, which be prioritized above the `.yml` file. The `default.env.yml` file provides fallback values 
which are used for any fields that are not supplied in the OS environment or in a `env.yml` file.

## File Host Settings

### `API_GOOGLE: "your-api-key-here"`

:   A Google Drive API key, this key is ordinarily pulled from the Hexproof API which provides
    a rotating API key to the app at runtime with limited permissions. This key is only used to
    request the metadata of Proxyshop templates hosted on Google Drive when using the Updater. If 
    you provide your own Google Drive API key here the app will use it instead and skip the launch 
    step which pulls a rotating key from Hexproof API.

### `API_AMAZON: "https://your-cloudfront-or-s3-url-here.com"`

:   Unlike the Google key, this field is a URL. This URL is ordinarily pulled from the Hexproof API as
    a rotating cloudfront URL where Proxyshop templates are hosted. We use S3+Cloudfront to host base app
    templates since Google Drive applies rate limits to downloading public files. If you would like to re-host
    Proxyshop templates (or your own templates) you can upload them to S3 and provide the base URL here. Almost 
    no one will ever need to use this variable, but if you do it is recommended to use Cloudfront to cache the S3
    files and provide the Cloudfront URL here instead of the direct S3 url. Cloudfront cached files are much cheaper
    on egress traffic than direct from S3.

## Photoshop Settings

### `PS_ERROR_DIALOG: False`

:   If this field is set to `True`, any actions executed by the app in Photoshop that fail due to an error will
    produce an error dialog in Photoshop if supported. This value should be `False` in production, since error dialogs
    will prevent further automation until they are dismissed. In a development environment it can be useful to set this
    value to `True`, especially when testing complex Photoshop behaviors, since the dialog may provide more context as 
    to why an action failed.

### `PS_VERSION: "2024"`

:   You can set this field to a year or a Photoshop version (Photoshop 2024 is version 180) to try and ensure Proxyshop
    uses a specific Photoshop version if you have multiple different copies of Photoshop installed. Unfortunately, this
    is not guaranteed to work and can prove unreliable on some systems. Generally, it is better to leave this value as
    null and open the version of Photoshop you wish to use before you launch Proxyshop (if Photoshop is already running, 
    the API will typically automatically link with that one).

## App Testing

### `HEADLESS: False`

:   When set to "True", Proxyshop will launch in CLI mode instead of GUI mode. At the moment this variable is not 
    really useful, since the CLI application can already be invoked when the Poetry environment is active using 
    `proxyshop <command>` and automatically governs Headless vs GUI mode where necessary.

### `DEV_MODE: False`

:   Right now this primarily governs logging output to console, but this will have wider implications in the future. 
    Generally speaking, if you're using the Proxyshop source code (Python version) instead of an official release, you
    probably want to set this field to `True`. There's no downside, only more verbose logging and other potentially 
    helpful features in the future.

### `TEST_MODE: False`

:   When set to "True", Proxyshop will use a modified GUI where the main card rendering menu is replaced with a 
    testing suite. The test suite can run targeted or mass render tests on one or more templates to card rendering 
    is working as it should be. Only enable this when you're ready to test a new or modified template for stability.

## Experimental

These features are considered experimental, may not provide any real use, and may be removed from the app at any time.

### `FORCE_RELOAD: False`

:   The intended use for enabling this is to force plugin templates to clear the associated plugin Python module and any 
    associated modules from the Python namespace completely and reimport them on each subsequent render operation. This 
    can be useful when editing and testing code on-the-fly, as you won't have to relaunch the app for consecutive tests.

### `VERSION: 1.14.0`

:   Replaces Photoshop's project version with a version string you provide. Can be useful when building alpha or beta 
    releases without having to bump the version number where Git is concerned (Proxyshop's version is typically 
    governed by the version listed in the `pyproject.toml` project file, which is automatically managed by commitizen.
