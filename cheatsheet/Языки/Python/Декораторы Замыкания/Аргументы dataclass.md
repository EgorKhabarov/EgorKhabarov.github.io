<div class="code-element">
    <div class="lang-line">python<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span>
</pre></div></div>
</div>

<p>dataclass(*,
          init: bool = ...,
          repr: bool = ...,
          eq: bool = ...,
          order: bool = ...,
          unsafe_hash: bool = ...,
          frozen: bool = ...)</p>
<p>init         Нужно ли автоматически генерировать метод <strong>init</strong> для инициализации атрибутов класса.
repr         Нужно ли автоматически генерировать метод <strong>repr</strong> для вывода строкового представления объектов класса.
eq           Нужно ли автоматически генерировать метод <strong>eq</strong> для сравнения объектов класса.
order        Нужно ли автоматически генерировать методы <strong>lt</strong>, <strong>le</strong>, <strong>gt</strong>, <strong>ge</strong> для сравнения объектов класса.
unsafe_hash  Нужно ли автоматически генерировать метод <strong>hash</strong> для объектов класса.
             Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы (frozen),
             так как изменяемые объекты могут привести к неожиданным результатам.
frozen       Нужно ли сделать объекты класса неизменяемыми (immutable).</p>
<p>Все эти аргументы являются необязательными, и если их не указывать,
то будут использованы значения по умолчанию (True для init, repr, eq, order, unsafe_hash и False для frozen).</p>