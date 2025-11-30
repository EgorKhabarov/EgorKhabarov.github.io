
Чтобы поменять цвет иконки папки
```css
#folder_list [data-kpath="Other/GitHub"] > svg > use {color: violet;}
```

Чтобы поменять цвет иконки файла
```css
#folder_list [data-vpath="Other/GitHub/Markdown"] > svg > use {color: blue;}
```

Шторки на всю ширину
```css
@media (max-width: 768px) {
    #cheatsheet_buttons, #toc_sidebar {
        max-width: 100%!important;
        width: 100%!important;
    }
}
```
