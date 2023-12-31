---

### # Калькулятор следующего времени выполнения задания по расписанию (Cron)</br>

Данный Python-программа рассчитывает следующую дату выполнения на основе матрицы расписания в стиле crontab.</br>

---

#### ## Общая информация</br>

Матрица расписания определяет интервалы для периодического выполнения задач:</br>

- **Первая строка:** Интервалы в 15 минут</br>
- **Вторая строка:** Почасовые интервалы</br>
- **Третья строка:** Дни недели</br>
- **Четвертая строка:** Дни месяца</br>
- **Пятая строка:** Месяцы года</br>

---

#### ## Формат ввода</br>

Строка расписания представляет собой текстовую переменную, в которой все выбранные ячейки перечислены. Ячейки разделены символом «,» (запятой), а строки разделены символом «;» (точкой с запятой). Например: `0,45;0,4,8,12,17,22;2,6;1,2,3,4,5,11,18,24;1,2,3,9,11;`</br>

_Примечание:_ В данном примере используется американский календарь, в котором 1 – это воскресенье, 2 – понедельник и т.д.</br>

---

#### ## Пример использования</br>

- **Дата отсчета:** 09.07.2010 23:36</br>  
- **Строка расписания:** `0,45;12;1,2,6;3,6,14,18,21,24,28;1,2,3,4,5,6,7,8,9,10,11,12;`</br>
- **Результат:** 18.07.2010 12:00</br>

---

#### ## Запуск программы</br>

Для запуска программы выполните следующие шаги:</br>

1. Убедитесь, что у вас установлен Python.</br>
2. Запустите файл программы.</br>
3. Введите начальную дату и строку расписания при необходимости.</br>
4. Получите результат - дату и время следующего запуска задачи.</br>

---
