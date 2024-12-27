<h1>ACID</h1>
<p>Основы транзакций в базах данных</p>
<p><strong>ACID</strong> — это набор свойств, которые обеспечивают надежность и корректность транзакций в базах данных</p>
<h3>Atomicity (Атомарность)</h3>
<p><strong>Всё или ничего</strong> Транзакция выполняется полностью или не выполняется вовсе
<strong>Если ошибка -&gt; откат всех изменений</strong> Если происходит сбой, система гарантирует откат всех изменений, чтобы база данных осталась в корректном состоянии</p>
<h3>Consistency (Согласованность)**</h3>
<p><strong>Транзакция переводит базу в согласованное состояние</strong> После выполнения транзакции база данных переходит из одного согласованного состояния в другое
<strong>Ограничения целостности соблюдены</strong> Внутренние правила базы (например, ограничения целостности) остаются соблюдены</p>
<h3>Isolation (Изолированность)**</h3>
<p><strong>Транзакции независимы</strong> Одновременное выполнение нескольких транзакций не влияет на их результат
<strong>Никаких "грязных" данных между транзакциями</strong> Каждая транзакция выполняется так, как если бы она была единственной в системе</p>
<h3>Durability (Долговечность)**</h3>
<p>После подтверждения транзакции её изменения сохраняются, даже если произойдет сбой системы</p>
<h2>Пример</h2>
<p>Допустим, мы переводим деньги с одного счёта на другой</p>
<ul>
<li><strong>Atomicity</strong>: Если произошёл сбой, то либо оба изменения (списание и зачисление) будут отменены, либо выполнены вместе</li>
<li><strong>Consistency</strong>: Сумма денег на обоих счетах остаётся одинаковой до и после транзакции</li>
<li><strong>Isolation</strong>: Другие транзакции не видят промежуточных состояний, например, когда деньги списаны, но ещё не зачислены</li>
<li><strong>Durability</strong>: После подтверждения транзакции данные о переводе сохранятся даже при сбое системы</li>
</ul>