# :material-head-question-outline: FAQ

???+ question "How do I download the Proxyshop templates manually?"

    If you wish to download the templates manually, visit [this link](https://drive.google.com/drive/u/1/folders/1sgJ3Xu4FabxNgDl0yeI7OjDZ7fqlI4p3). 
    These archives must be extracted to the `/templates` directory. The archives found within the **Investigamer** and 
    **SilvanMTG** drive folders must be extracted to `/plugins/Investigamer/templates` and 
    `/plugins/SilvanMTG/templates` respectively.

???+ question "How do I change the set symbol to something else?"

    In settings, change "Default Symbol" to the set code of the symbol you want, and enable "Force Default Symbol".
    If you wish to add a totally custom symbol, here's the process:

    - Head over to `src/img/symbols/` and create a folder named according a new custom code.
    - Add your custom SVG symbols to the folder you created, name each file according to the first letter of its rarity (capitalized).
    - Set that symbol as "Default Symbol" and enabled "Force Default Symbol". You're good to go!

???+ question "How do I completely hide the set symbol?"

    In Global Settings, or settings for a specific template, change "Symbol Render Mode" to None. This disables the expansion symbol altogether.

???+ question "How do I hide a layer in a Proxyshop template, so it doesn't appear in rendered cards?"

    In the Photoshop template of your choice, change the opacity to 0 on the layer you wish to hide.
    You can use this method to hide anything. This is safer than just disabling the layer's visibility because layers
    may be forcibly enabled and disabled by the app, it's also safer than deleting the layer because that
    may cause errors on some templates.

???+ question " Where is a good place to find high quality MTG art?"
  
    Your best resource is going to be [MTG Pics](https://mtgpics.com), to improve art quality even more you can look 
    into upscaling with Topaz/Chainner/ESRGAN. On our [discord](https://discord.gg/magicproxies) we provide a lot of 
    resources for learning how to upscale art easily and effectively. For mass downloading art, view my other project: 
    [MTG Art Downloader](https://github.com/Investigamer/mtg-art-downloader)
  
???+ question "The app stops when trying to enter text and Photoshop becomes unresponsive!"

    There is a known [bug](https://github.com/MrTeferi/MTG-Proxyshop/issues/9) where Photoshop crashes when trying to enter too much text into a text box, it should be fixed but could theoretically happen on some plugin templates that don't make the text box big enough.
    The best way to fix this is to open the template in Photoshop and expand the bottom edge of the Rules text boxes (creature and noncreature).

???+ question "Required value is missing / RPC server not responding."

    This can sometimes be one of the more rare but obnoxious errors that occur on some systems. Sometimes the root cause is unknown, but it can
    usually be fixed. Try these options in order until something works:
    
    - Ensure there is only **ONE** installation of Photoshop on your computer. Having two versions of Photoshop installed at the same time can prevent making a connection to the app. If you have more than one installed, uninstall **all** versions of Photoshop and reinstall one version. You must uninstall all of them **first**, just removing one likely won't fix the issue.
    - Ensure that your Photoshop application was installed using an actual installer. **Portable installations** of Photoshop do not work with Proxyshop, since Windows needs to know where it is located.
    - Close Photoshop and Proxyshop, then run both Photoshop and Proxyshop as Administrator, try rendering something.
    - Close both of them, then hold ALT + CTRL + SHIFT while launching Photoshop, then launch Proxyshop, try again.
    - Restart your computer, then start both and try again.
    - If you have a particularly over-defensive antivirus software running that may be interfering with Proxyshop 
    connecting to Photoshop, such as Avast, Norton, etc. close your antivirus software, relaunch both, and try again. You might also try disabling Windows Defender.
    - If there's a chance your Photoshop installation could be damaged, corrupted, or otherwise messed up in some way, it is recommended to completely uninstall Photoshop and install the latest version you have access to. 
    Generally, Proxyshop works best with newer versions of Photoshop. If using an in-authentic version of Photoshop, verify it is of high quality and uses a real installer.
    - If all of these fail to fix the issue, please join our Discord (linked at the top) and provide the error log from `logs/error.txt` in
    your Proxyshop directory, so we can help find the cause :)

???+ question "Mana Cost, Rules, or other text is huge and not scaling down?"

    - In Photoshop go to **Edit** > **Preferences** > **Units & Rulers**.
    - Set **Rulers** to **Pixels**
    - Set **Type** to **Points**
    - The issue should be fixed.

???+ question "Photoshop is busy!"

    This error occurs when Photoshop is not responding to commands because it is busy.
    To prevent this error, you must ensure Photoshop is in a neutral state when you run Proxyshop or render a card:
    
    - There should be no dialog boxes or settings menus open in Photoshop. The normal tool panels are fine.
    - There should be no tools performing tasks, for example having text highlighted for editing with the text tool.
    - Ideally Photoshop should be launched fresh, with no documents open.

???+ question "I'm getting some other error!"

    In your proxyshop directory, look for a folder named `logs`, inside that folder you should see `error.txt`, check 
    the last error log in that file. If the error isn't obvious, [join our Discord](https://discord.gg/magicproxies) 
    and feel free to ask for help in the [#Proxyshop](https://discord.com/channels/889831317066358815/953423615091683368) channel.
