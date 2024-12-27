<p>Лямбда-выражение можно использовать только совместно с функциональными интерфейсами.
Функциональный интерфейс — это интерфейс, описывающий только один метод, который необходимо переопределить.
Внутри такого интерфейса могут быть методы по умолчанию с реализацией, статические методы и статические константы.
Чтобы явно определить функциональный интерфейс, перед объявлением следует указать аннотацию</p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="nd">@FunctionalInterface</span>
</pre></div></div></div>
<p>Она не является обязательной, но позволит избежать различных ошибок — например, добавления объявлений дополнительных абстрактных методов.</p>
<p>Java 8 существует целый пакет, содержащий множество готовых функциональных интерфейсов
<a href="?Languages/Java/java/util/function/">java.util.function</a></p>