# Quadratic Equation Solver

Цей застосунок розв'язує квадратні рівняння виду:

    ax^2 + bx + c = 0

Підтримується інтерактивний та неінтерактивний (файловий) режим роботи.

## Інструкція запуску

### Інтерактивний режим

Запустіть програму без аргументів:

    python main.py

Вас попросять ввести коефіцієнти a, b, c. Якщо введено некоректне значення, програма попросить ввести ще раз.

### Неінтерактивний (файловий) режим

Запустіть програму з одним аргументом — шляхом до файлу з коефіцієнтами:

    python main.py test_valid.txt

## Формат файлу для неінтерактивного режиму

У файлі має бути один рядок:

    a b c\n

- Коефіцієнти розділені одним пробілом
- Десятковий роздільник — крапка
- Після останнього числа — символ нового рядка (\n)

**Приклад:**

    1 0 0\n

## Revert-коміт

Посилання на revert-коміт: `<b1d08e68f4cfdf44f6c80a6fb473241a02ddb5a8>`

## Опис комітів

- 