# SD


Хорошая реализация. Легко-масштабируемая, справился за несколько минут.

Оказалось удобным:
* отдельный файл для каждой команды, очевидны точки расширения
* смена директории без дополнительных сложностей
* хорошее описание архитектуры
* отличные тесты

Оказалось неудобным:
* разное поведение при передаче параметров в случае 0 и большем кол-ве

Можно улучшить:
* большая вложенность кода, кажется в некоторых случаях лучше разнести на отдельные функции