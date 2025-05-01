function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.getElementById('add-status-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/status/add/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const table = document.getElementById('status-table');
                const row = document.createElement('tr');
                row.setAttribute('data-id', data.id);
                row.innerHTML = `
                <td>${data.name}</td>
                <td>
                    <button class="btn btn-sm btn-warning edit-status" data-bs-toggle="modal" data-bs-target="#editStatusModal" data-id="${data.id}" data-name="${data.name}">Редактировать</button>
                    <button class="btn btn-sm btn-danger delete-status" data-bs-toggle="modal" data-bs-target="#deleteStatusModal" data-id="${data.id}" data-name="${data.name}">Удалить</button>
                </td>
            `;
                table.appendChild(row);
                bootstrap.Modal.getInstance(document.getElementById('addStatusModal')).hide();
                this.reset();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

document.querySelectorAll('.edit-status').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('edit-status-id').value = this.dataset.id;
        document.getElementById('edit-status-name').value = this.dataset.name;
    });
});

document.getElementById('edit-status-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/status/edit/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const row = document.querySelector(`#status-table tr[data-id="${data.id}"]`);
                row.querySelector('td').textContent = data.name;
                row.querySelector('.edit-status').dataset.name = data.name;
                row.querySelector('.delete-status').dataset.name = data.name;
                bootstrap.Modal.getInstance(document.getElementById('editStatusModal')).hide();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

// Обработка удаления статуса
document.querySelectorAll('.delete-status').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('delete-status-id').value = this.dataset.id;
        document.getElementById('delete-status-name').textContent = this.dataset.name;
    });
});

document.getElementById('delete-status-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/status/delete/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.querySelector(`#status-table tr[data-id="${formData.get('id')}"]`).remove();
                bootstrap.Modal.getInstance(document.getElementById('deleteStatusModal')).hide();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

// Обработка добавления типа
document.getElementById('add-type-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/type/add/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const table = document.getElementById('type-table');
                const row = document.createElement('tr');
                row.setAttribute('data-id', data.id);
                row.innerHTML = `
                <td>${data.name}</td>
                <td>
                    <button class="btn btn-sm btn-warning edit-type" data-bs-toggle="modal" data-bs-target="#editTypeModal" data-id="${data.id}" data-name="${data.name}">Редактировать</button>
                    <button class="btn btn-sm btn-danger delete-type" data-bs-toggle="modal" data-bs-target="#deleteTypeModal" data-id="${data.id}" data-name="${data.name}">Удалить</button>
                </td>
            `;
                table.appendChild(row);
                bootstrap.Modal.getInstance(document.getElementById('addTypeModal')).hide();
                this.reset();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

document.querySelectorAll('.edit-type').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('edit-type-id').value = this.dataset.id;
        document.getElementById('edit-type-name').value = this.dataset.name;
    });
});

document.getElementById('edit-type-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/type/edit/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const row = document.querySelector(`#type-table tr[data-id="${data.id}"]`);
                row.querySelector('td').textContent = data.name;
                row.querySelector('.edit-type').dataset.name = data.name;
                row.querySelector('.delete-type').dataset.name = data.name;
                bootstrap.Modal.getInstance(document.getElementById('editTypeModal')).hide();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

// Обработка удаления типа
document.querySelectorAll('.delete-type').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('delete-type-id').value = this.dataset.id;
        document.getElementById('delete-type-name').textContent = this.dataset.name;
    });
});

document.getElementById('delete-type-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/type/delete/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.querySelector(`#type-table tr[data-id="${formData.get('id')}"]`).remove();
                bootstrap.Modal.getInstance(document.getElementById('deleteTypeModal')).hide();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

document.getElementById('add-category-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/category/add/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const table = document.getElementById('category-table');
                const row = document.createElement('tr');
                row.setAttribute('data-id', data.id);
                row.innerHTML = `
                <td>${data.full_name}</td>
                <td>${data.type_name}</td>
                <td>${data.parent_name || '—'}</td>
                <td>
                    <button class="btn btn-sm btn-warning edit-category" data-bs-toggle="modal" data-bs-target="#editCategoryModal" data-id="${data.id}" data-name="${data.name}" data-type="${data.type}" data-parent="${data.parent || ''}">Редактировать</button>
                    <button class="btn btn-sm btn-danger delete-category" data-bs-toggle="modal" data-bs-target="#deleteCategoryModal" data-id="${data.id}" data-name="${data.name}">Удалить</button>
                </td>
            `;
                table.appendChild(row);
                bootstrap.Modal.getInstance(document.getElementById('addCategoryModal')).hide();
                this.reset();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

document.querySelectorAll('.edit-category').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('edit-category-id').value = this.dataset.id;
        document.getElementById('edit-category-name').value = this.dataset.name;
        document.getElementById('edit-category-type').value = this.dataset.type;
        document.getElementById('edit-category-parent').value = this.dataset.parent || '';
    });
});

document.getElementById('edit-category-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/category/edit/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const row = document.querySelector(`#category-table tr[data-id="${data.id}"]`);
                row.querySelectorAll('td')[0].textContent = data.full_name;
                row.querySelectorAll('td')[1].textContent = data.type_name;
                row.querySelectorAll('td')[2].textContent = data.parent_name || '—';
                const editButton = row.querySelector('.edit-category');
                editButton.dataset.name = data.name;
                editButton.dataset.type = data.type;
                editButton.dataset.parent = data.parent || '';
                row.querySelector('.delete-category').dataset.name = data.name;
                bootstrap.Modal.getInstance(document.getElementById('editCategoryModal')).hide();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});

document.querySelectorAll('.delete-category').forEach(button => {
    button.addEventListener('click', function () {
        document.getElementById('delete-category-id').value = this.dataset.id;
        document.getElementById('delete-category-name').textContent = this.dataset.name;
    });
});

document.getElementById('delete-category-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/references/category/delete/', {
        method: 'POST', headers: {'X-CSRFToken': csrftoken}, body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.querySelector(`#category-table tr[data-id="${formData.get('id')}"]`).remove();
                bootstrap.Modal.getInstance(document.getElementById('deleteCategoryModal')).hide();
            } else {
                alert('Ошибка: ' + data.error);
            }
        })
        .catch(error => console.error('Ошибка:', error));
});