# ДОМАШНЕЕ ЗАДАНИЕ ПО МОНИТОРИНГУ

```
namespace: sre-cource-student-74
user: student74
```
## Структура проекта



## Установка компонентов

Для установки prometheus, node_exporter и black_box_exporter я использовал ansible.

За основу взял роли с этого ресурса https://github.com/MiteshSharma/PrometheusWithAnsible. 

Далее добавил роль alertmanager из репозитория https://github.com/prometheus-community/ansible/tree/main/roles/alertmanager  

У patroni есть свой собственный экспортер "из коробки", буду использовать его:

10.0.10.5:8008 
10.0.10.6:8008 внес в прометей

http://10.0.10.2:2379/metrics

![Схема](.png)

