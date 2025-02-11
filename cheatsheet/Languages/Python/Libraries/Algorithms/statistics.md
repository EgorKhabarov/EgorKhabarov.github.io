# statistics

Библиотека **statistics** в Python предоставляет функции для выполнения математических вычислений, связанных со статистикой

| Имя                 | Описание                                                                                             |
|---------------------|------------------------------------------------------------------------------------------------------|
| `NormalDist`        | Нормальное распределение (Гауссово). Поддерживает методы для вычисления вероятностей и распределений |
| `StatisticsError`   | Ошибка, возникающая при недопустимых статистических вычислениях                                      |
| `correlation`       | Возвращает коэффициент корреляции Пирсона для двух наборов данных                                    |
| `covariance`        | Вычисляет ковариацию двух наборов данных                                                             |
| `geometric_mean`    | Вычисляет геометрическое среднее значений                                                            |
| `harmonic_mean`     | Вычисляет гармоническое среднее значений                                                             |
| `kde`               | Возвращает ядерную плотность распределения для заданного набора данных                               |
| `kde_random`        | Генерирует случайные значения на основе ядерной плотности распределения                              |
| `linear_regression` | Выполняет линейную регрессию, возвращая коэффициенты наклона и смещения                              |
| `mean`              | Возвращает среднее арифметическое                                                                    |
| `fmean`             | Возвращает среднее арифметическое (быстрее, чем `mean`)                                              |
| `median`            | Вычисляет медиану значений                                                                           |
| `median_grouped`    | Вычисляет сгруппированную медиану (медиана в пределах определённых интервалов)                       |
| `median_high`       | Возвращает "высокую" медиану — значение из правой части отсортированного списка                      |
| `median_low`        | Возвращает "низкую" медиану — значение из левой части отсортированного списка                        |
| `mode`              | Определяет моду — наиболее часто встречающееся значение                                              |
| `multimode`         | Возвращает список всех мод                                                                           |
| `pstdev`            | Вычисляет стандартное отклонение для генеральной совокупности                                        |
| `pvariance`         | Вычисляет дисперсию для генеральной совокупности                                                     |
| `quantiles`         | Разбивает данные на интервалы, используя метод квантилей                                             |
| `stdev`             | Вычисляет стандартное отклонение для выборки                                                         |
| `variance`          | Вычисляет дисперсию для выборки                                                                      |

---

### NormalDist
```python
from statistics import NormalDist

nd = NormalDist(mu=0, sigma=1)  # Нормальное распределение с μ=0 и σ=1
print(nd.pdf(0))  # Плотность вероятности в точке 0
print(nd.cdf(1))  # Вероятность, что значение <= 1
```

### StatisticsError
```python
from statistics import mean, StatisticsError

try:
    print(mean([]))  # Ошибка: пустая последовательность
except StatisticsError as e:
    print(f"Ошибка: {e}")
```

### correlation
```python
from statistics import correlation

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
print(correlation(x, y))  # Результат: 1.0 (идеальная линейная зависимость)
```

### covariance
```python
from statistics import covariance

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
print(covariance(x, y))  # Ковариация: 2.666...
```

### fmean
```python
from statistics import fmean

data = [1, 2, 3, 4, 5]
print(fmean(data))  # Быстрое среднее арифметическое: 3.0
```

### geometric_mean
```python
from statistics import geometric_mean

data = [1, 2, 3, 4, 5]
print(geometric_mean(data))  # Геометрическое среднее: ~2.605
```

### harmonic_mean
```python
from statistics import harmonic_mean

data = [1, 2, 3, 4, 5]
print(harmonic_mean(data))  # Гармоническое среднее: ~2.189
```

### kde
```python
from statistics import kde

data = [1, 2, 2, 3, 4]
kde_func = kde(data)
print(kde_func(2.5))  # Значение плотности в точке 2.5
```

### linear_regression
```python
from statistics import linear_regression

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
slope, intercept = linear_regression(x, y)
print(f"y = {slope}x + {intercept}")  # Линейное уравнение: y = 2.0x + 0.0
```

### mean
```python
from statistics import mean

data = [1, 2, 3, 4, 5]
print(mean(data))  # Среднее арифметическое: 3.0
```

### median
```python
from statistics import median

data = [1, 3, 5, 7, 9]
print(median(data))  # Медиана: 5
```

### median_grouped
```python
from statistics import median_grouped

data = [1, 2, 2, 2, 3]
print(median_grouped(data))  # Группированная медиана: 2.0
```

### median_high / median_low
```python
from statistics import median_high, median_low

data = [1, 3, 5, 7]
print(median_high(data))  # Высокая медиана: 5
print(median_low(data))   # Низкая медиана: 3
```

### mode / multimode
```python
from statistics import mode, multimode

data = [1, 2, 2, 3, 3, 4]
print(mode(data))       # Мода: 2 (первое встречающееся значение)
print(multimode(data))  # Все моды: [2, 3]
```

### pstdev / pvariance
```python
from statistics import pstdev, pvariance

data = [1, 2, 3, 4, 5]
print(pstdev(data))    # Стандартное отклонение (популяция): ~1.414
print(pvariance(data)) # Дисперсия (популяция): 2.0
```

### stdev / variance
```python
from statistics import stdev, variance

data = [1, 2, 3, 4, 5]
print(stdev(data))     # Стандартное отклонение (выборка): ~1.581
print(variance(data))  # Дисперсия (выборка): 2.5
```

### quantiles
```python
from statistics import quantiles

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(quantiles(data, n=4))  # Квартильные значения: [2.5, 5.0, 7.5]
```
