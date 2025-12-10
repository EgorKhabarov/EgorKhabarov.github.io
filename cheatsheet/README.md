<div>
    <h1>Cheat sheet</h1>
    <a href="https://github.com/EgorKhabarov/EgorKhabarov.github.io"><img alt="GitHub Pages badge" src="src/badge.svg" class="unselectable" style="height:1.667em;"/></a>
    <p>This is a site with cheat sheets</p>
</div>

## Keyboard

### Settings

Press <kbd style="cursor: pointer;" onclick="toggleSettings(true);">Ctrl + I</kbd> to open **settings**

### Search

Press <kbd style="cursor: pointer;" onclick="page_search_container.style.display='flex';mainInput.focus();pulseHighlight(mainInput);">Ctrl + F</kbd> to open **Find in page search**
To search using <a href="?Languages/RegExp/RegExp">regular expressions</a>, write a query in the format <code class="code_no_copy" style="cursor: pointer;" onclick="page_search_container.style.display='flex';mainInput.focus();mainInput.value='//pattern/flags/';mainInput.dispatchEvent(new Event('input'));">/pattern/flags</code>

Press <kbd style="cursor: pointer;" onclick="leftDrawer.open();sidebarInput.focus();pulseHighlight(sidebarInput);">Ctrl + Shift + F</kbd> to open **global search**
This is a [full-text search](https://en.wikipedia.org/wiki/Full-text_search) by both cheat sheet names and their contents 

> [!TIP]
> You can refine your full-text search using:

> <code>+word</code> - the result must include this word
> <code>-word</code> - the result must NOT include this word
> <code>word*</code> - match words starting with this term
> <code>word~1</code> - fuzzy match (distance 1)
> <code>word^2</code> - boost word importance

> Examples:
> <code>+apple juice\*</code><br>
> <code>banana~1 -rotten</code><br>
> <code>apple^2 fresh\*</code><br>

## Customization

You can insert your own CSS code in the settings
[Here](?Snippets/CSS/cheatsheet_snippets) you can find examples and frequently used CSS snippets
If a softlock occurs, you can go to <a href="/cheatsheet/reset" target="_self">/cheatsheet/reset</a>

## Creating cheat sheets and checking markup

You can see what all supported markup options look like [here](?Other/MARKUP_EXAMPLES)
