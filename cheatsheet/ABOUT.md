# ABOUT

This is a site with cheat sheets

### Keyboard

Press <kbd style="cursor: pointer;" onclick="floating_search.style.display='flex';mainInput.focus();">Ctrl + F</kbd> to open **Find in page search**
To search using <a href="?Languages/RegExp/RegExp">regular expressions</a>, write a query in the format <code class="code_no_copy" style="cursor: pointer;" onclick="floating_search.style.display='flex';mainInput.focus();mainInput.value='//pattern/flags/';mainInput.dispatchEvent(new Event('input'));">/pattern/flags</code>

Press <kbd style="cursor: pointer;" onclick="openSidebar();sidebarInput.focus();">Ctrl + Shift + F</kbd> to open **global search**
This is a full-text search by both cheat sheet names and their contents 

> [!TIP]
> You can refine your search using:

> <code>+word</code> - the result must include this word
> <code>-word</code> - the result must NOT include this word
> <code>word*</code> - match words starting with this term
> <code>word~1</code> - fuzzy match (distance 1)
> <code>word^2</code> - boost word importance

> Examples:
> <code>+apple juice\*</code><br>
> <code>banana~1 -rotten</code><br>
> <code>apple^2 fresh\*</code><br>

**Below is the debug section for viewing the correctness of the markup**

# Headers

# `#` 1
## `##` 2
### `###` 3
#### `####` 4
##### `#####` 5
###### `######` 6

---

# Highlighting

\*Italic\* - *Italic*
\_Italic\_ - _Italic_

\*\*Bold\*\* - **Bold**
\_\_Bold\_\_ - __Bold__

\*\*\*Bold & Italic\*\*\* - ***Bold & Italic***
\_\_\_Bold & Italic\_\_\_ - ___Bold & Italic___
\*\*\_Bold & Italic\_\*\* - **_Bold & Italic_**
\_\*\*Bold & Italic\*\*\_ - _**Bold & Italic**_

\`text\` - `text`

\|\|text\|\| - ||text||

&#x7e;&#x7e;text&#x7e;&#x7e; - ~~text~~

&#x3d;&#x3d;mark&#x3d;&#x3d; - ==mark==

&#x3d;&#x3d;{color:red;background-color:inherit;}mark&#x3d;&#x3d; - =={color:red;background-color:inherit;}mark==

`---` or `<hr>`

---

---

# Table

<div class="container-row">

```pre
code
```
&nbsp;&nbsp;
````pre
```pre
code
```
````
&nbsp;&nbsp;
`````pre
````pre
```pre
code
```
````
`````

</div>

```table
| c1 | c2 |
|----|----|
| v1 | v2 |
| v3 | v4 |
```

| c1 | c2 |
|----|----|
| v1 | v2 |
| v3 | v4 |

```table
|    |    |
|----|----|
| v1 | v2 |
| v3 | v4 |
```

|    |    |
|----|----|
| v1 | v2 |
| v3 | v4 |

# Blockquote

blockquote 1

> blockquote 1

blockquote 2

>> blockquote 2

blockquote 3

> blockquote 1
>> blockquote 2
>>> blockquote 3

## Alerts

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming content

> [!TIP]
> Helpful advice for doing things better or more easily

> [!IMPORTANT]
> Key information users need to know to achieve their goal

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions
```

Read more [here](?Other/GitHub/Markdown) and [here](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

blockquote NOTE

> [!NOTE]
> Useful information that users should know, even when skimming content

blockquote TIP

> [!TIP]
> Helpful advice for doing things better or more easily

blockquote IMPORTANT

> [!IMPORTANT]
> Key information users need to know to achieve their goal

blockquote WARNING

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems

blockquote CAUTION

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions

blockquote WARNING

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems
>> 123
>>> qweret
> r
> 1234tv

---

# SVG

<table><thead><tr><th style="text-align: center;">Icon</th><th style="text-align: left;">Description</th></tr></thead><tbody>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-yellow);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-yellow);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Обычная папка</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-white);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-white);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Обычная шпаргалка</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-green);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-green);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Библиотека</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-red);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-red);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Важное</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-pink);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-pink);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;"></td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-violet);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-violet);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Язык</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-dblue);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-dblue);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;"></td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-lblue);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-lblue);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Картинки</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-brown);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-brown);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Примеры кода</td></tr>

</tbody></table>
