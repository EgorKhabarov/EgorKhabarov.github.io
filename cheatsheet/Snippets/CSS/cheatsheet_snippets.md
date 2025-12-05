### Change the color of the folder icon
```css
#folder_list [data-kpath="Other/GitHub"] > svg > use {color: violet;}
```
### Change the color of the file icon
```css
#folder_list [data-vpath="Other/GitHub/Markdown"] > svg > use {color: blue;}
```
### Шторки на всю ширину
```css
@media (max-width: 768px) {
    #cheatsheet_buttons, #toc_sidebar {
        max-width: 100%!important;
        width: 100%!important;
    }
}
```
### Remove the cheat sheet width limitation
```css
.cheatsheet_field {max-width: 100%;}
```
### Accent color
```css
:root {--accent-color: #3B82F6;}
[data-theme="dark"] {--accent-color: #005FCC;}
```
```css
:root{--accent-color: #2394878C}
```
