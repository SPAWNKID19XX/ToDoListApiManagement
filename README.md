# ToDoListApiManagement
## 🎯 Тестовое задание: API для управления задачами (To-Do List)

### 🔧 Описание:
Создать REST API для управления задачами с использованием Django + DRF.

### 📋 Функционал:
1. **Модели:**
   - `User` (стандартная модель Django)
   - `Task` с полями:
     - `title` (CharField)
     - `description` (TextField, optional)
     - `status` (ChoiceField: 'todo', 'in_progress', 'done')
     - `priority` (ChoiceField: 'low', 'medium', 'high')
     - `created_at` (DateTimeField)
     - `updated_at` (DateTimeField)
     - `assigned_to` (ForeignKey к User)

2. **API endpoints:**
   - `GET /api/tasks/` — список задач
   - `GET /api/tasks/{id}/` — детали задачи
   - `POST /api/tasks/` — создать задачу
   - `PUT /api/tasks/{id}/` — обновить задачу
   - `DELETE /api/tasks/{id}/` — удалить задачу
   - `GET /api/tasks/?status=done` — фильтрация по статусу
   - `GET /api/tasks/?assigned_to={user_id}` — фильтрация по пользователю

3. **Дополнительно:**
   - Аутентификация (JWT или Token)
   - Права доступа (только владелец задачи или админ может редактировать)
   - Валидация данных
   - Pagination

### ✅ Требования:
- Использовать DRF Serializers, ViewSets, Routers
- Реализовать фильтрацию и сортировку
- Добавить тесты (pytest или unittest)

### 📝 Что оценивается:
- Архитектура проекта
- Качество кода
- Использование DRF
- Тестирование
- Оформление

---