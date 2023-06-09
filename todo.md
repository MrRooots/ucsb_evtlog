Разработать скрипт для сбора информации о создании и завершении
процессов пользователями на удалённом компьютере.
Использовать EventId 4688 и 4689 из журнала событий windows
(должен быть настроен аудит создания процессов).

Требования к перечню собираемых данных:

1. [+] Имя компьютера с которого поступили данные.
2. [+] Время возникновения события в формате "01.05.2029 11:06:42".
3. [+] Имя пользователя, инициировавшего событие.
4. [+] Имя домена пользователя.
5. [+] Sid.
6. [+] Имя процесса.
7. [+] Действие: "Запуск процесса" или "Завершение процесса".

Требования к среде разработки:

1. [+] Скрипт должен быть реализован на языке Python. [3.10]
2. [+] Могут быть использованы любые сторонние библиотеки. [requirements.txt]

Требования к результату: [Check src.config.Config]

1. На вход скрипта необходимо подавать обязательный параметр - имя
   или ip адрес удаленного компьютера.
2. На вход скрипта можно подать необязательный параметр - sid
   пользователя, тогда данные будут собраны только по этому
   конкретному пользователю.
3. На вход скрипта можно подать необязательный параметр — дата
   с которой начинается поиск событий, тогда будут собраны
   данные не старее указанной даты. Формат даты "01.05.2029".
4. На вход скрипта можно подать необязательный параметр — дата
   окончания поиска событий, тогда будут собраны данные не
   новее указанной даты. Формат даты "01.05.2029".
5. Представление собранных данных структурировано, понятно для
   оператора.
6. Результат сбора данных сохраняется в файл.

