# Localization Tool

Веб-приложение, которое позволяет переводить значения ключей в `.arb` файле

## Endpoints
* `/localization/local-from-json` - В качестве тела запроса и ответа используется json
* `/localization/local-from-file` - В качестве тела запроса и ответа используется .arb файл
* `/health` - Для проверки работы приложения

## Процесс перевода

Для перевода рекурсивно обходим json файл и находим все значения, которые являются строками и переводим их. Для перевода
используется библиотека `translators`, которая позволяет выбрать различные api для перевода. Наиболее адекватный перевод
получается при использовании `alibaba`

Для улучшения качества перевода было сделано следующее:
* Добавлено множество ключей, значения которых не нужно переводить
* Для строк, которые начинаются и заканчиваются с фигурной скобки переводится только часть состоящая из токенов вида `слово{слово или
предложение}`, так остальная часть используется при разработке и не должна быть переведена.
* `alibaba` был выбран, так как не переводит токены вида `{}`, которые находятся внутри строки

## Пример перевода №1

```json
{
  "pageHomeBalance" : "Your balance is {amount} on {date}",
  "@pageHomeBalance" : {
      "placeholders": {
          "amount": {
              "type": "double",
              "format": "currency",
              "example": "$1000.00",
              "description": "Account balance",
              "optionalParameters": {
                  "decimalDigits": 2,
                  "name": "USD",
                  "symbol": "$",
                  "customPattern": "¤#0.00"
              }
          },
          "date": {
              "type": "DateTime",
              "format": "yMd",
              "example": "11/10/2021",
              "description": "Balance date"
          }
      }
  }
}
```

```json
{
  "pageHomeBalance": "Ваш баланс составляет {amount} на {date}",
  "@pageHomeBalance": {
    "placeholders": {
      "amount": {
        "type": "double",
        "format": "currency",
        "example": "100, 00 долл. США",
        "description": "Баланс счета",
        "optionalParameters": {
          "decimalDigits": 2,
          "name": "USD",
          "symbol": "$",
          "customPattern": "¤#0.00"
        }
      },
      "date": {
        "type": "DateTime",
        "format": "yMd",
        "example": "11/10/2021",
        "description": "Дата баланса"
      }
    }
  }
}
```

## Пример перевода №2

```json
{
  "pageHomeInboxCount" : "{count, plural, zero{You have no new messages} one{You have 1 new message} other{You have {count} new messages}}",
  "@pageHomeInboxCount" : {
      "description" : "New messages count on the Home screen",
      "placeholders": {
          "count": {}
      }
  }
}
```

```json
{
  "pageHomeInboxCount": "{count, plural, Zero {У вас нет новых сообщений} одно {у вас есть 1 новое сообщение} другое {у вас есть {count} новые сообщения}}",
  "@pageHomeInboxCount": {
    "description": "Количество новых сообщений на главном экране",
    "placeholders": {
      "count": {}
    }
  }
}
```

## Пример перевода №3

```json
{
  "appName": "HelpOS Employee",
  "companyName": "Security-online",
  "drawerHome": "Home",
  "drawerTables": "Tables"
}
```

```json
{
  "appName": "Сотрудник HelpOS",
  "companyName": "Безопасность-онлайн",
  "drawerHome": "Дом",
  "drawerTables": "Столы"
}
```