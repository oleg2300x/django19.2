Задание 2
В сервисе реализуйте функционал аутентификации, а именно:

регистрацию пользователя по почте и паролю;
верификацию почты пользователя через отправленное письмо;
авторизацию пользователя;
восстановление пользователя на автоматически сгенерированный пароль.
Задание 3
Закройте для анонимных пользователей все контроллеры, которые отвечают за работу с продуктами. При этом создаваемые продукты должны автоматически привязываться к авторизованному пользователю.

Не забудьте добавить поле для продуктов, через которое пользователь будет привязываться. Текущий авторизованный пользователь доступен в любом контроллере через 
self.request.user
.